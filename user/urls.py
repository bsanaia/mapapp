from user import views
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.log_in, name='login'),
    path(r'^password_reset/', auth_views.password_reset, name='password_reset'),
    path(r'^password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('accounts/password/change/', auth_views.password_change, name='password_change'),
    path('accounts/password/change/done/', auth_views.password_change_done, name='password_change_done'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
