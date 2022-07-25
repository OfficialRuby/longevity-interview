from django.apps import AppConfig


class UserInputConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_input'

    def ready(self):
        import user_input.signals
