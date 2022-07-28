from django.urls import path
from reward.views import (IndexView, EarnRewardView, SupplyParameterView,
                          ConnectDeviceView, connect_device, disconnect_device, ConnectAppView, connect_app,
                          disconnect_app, TestLogin)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', TestLogin.as_view(), name='test'),
    path('earn-reward/', EarnRewardView.as_view(), name='earn_reward'),
    path('supply-parameters/', SupplyParameterView.as_view(), name='supply_param'),
    path('connect-devices/', ConnectDeviceView.as_view(), name='connect_device'),
    path('connect-apps/', ConnectAppView.as_view(), name='connect_app'),
    path('connect-device/<int:id>/', connect_device, name='connect_one_device'),
    path('disconnect-device/<int:id>/', disconnect_device, name='disconnect_one_device'),
    path('connect-app/<int:id>/', connect_app, name='connect_one_app'),
    path('disconnect-app/<int:id>/', disconnect_app, name='disconnect_one_app'),

]
