from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse

CONNECTION_CHOICES = (
    ('success', 'Connected'),
    ('danger', 'Not Connected'),
)
MEASURE_INSTRUMENT_CHOICES = (
    ('metric', 'Metric'),
    ('imperial', 'Imperial'),
    ('custom', 'Custom'),
)


class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward_point = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=150)
    date_awarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# As per the Figma, user can be rewarded on the following occassions
# 50 $LONG when the sign up
# 5 $LONG when they link an app
# 5 $LONG when they link a device
# 15 $LONG when they add disease
# 1 $LONG when they introduce themselves


class Device(models.Model):
    class Meta:
        verbose_name_plural = 'Devices'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='device')
    reward_point = models.PositiveIntegerField(default=5)
    awarded = models.BooleanField(default=False)
    date_awarded = models.DateTimeField(blank=True, null=True)
    battery_life = models.PositiveIntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)],
        blank=True, null=True)
    connection_status = models.CharField(max_length=30, choices=CONNECTION_CHOICES, default='danger')

    def __str__(self):
        return self.user.username

    def get_connect_url(self):
        return reverse('connect_one_device',
                       kwargs={
                           'id': self.id
                       })

    def get_disconnect_url(self):
        return reverse('disconnect_one_device',
                       kwargs={
                           'id': self.id
                       })


class Disease(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ManyToManyField('reward.Diseases')
    reward_point = models.PositiveIntegerField(default=15)


class Diseases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    symptoms = models.TextField()
    awarded = models.BooleanField(default=False)
    date_awarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Parameter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    measure_instrument = models.CharField(max_length=30, choices=MEASURE_INSTRUMENT_CHOICES, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reward_point = models.PositiveIntegerField(default=1)
    awarded = models.BooleanField(default=False)
    date_awarded = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='app')
    reward_point = models.PositiveIntegerField(default=5)
    awarded = models.BooleanField(default=False)
    date_awarded = models.DateTimeField(blank=True, null=True)
    connection_status = models.CharField(max_length=30, choices=CONNECTION_CHOICES, default='danger')

    def __str__(self):
        return self.user.username

    def get_connect_url(self):
        return reverse('connect_one_app',
                       kwargs={
                           'id': self.id
                       })

    def get_disconnect_url(self):
        return reverse('disconnect_one_app',
                       kwargs={
                           'id': self.id
                       })
