from django.urls import path
from .views import *

urlpatterns = [
    path("save-details/", save_details, name='save-details'),
    path("details/", details, name="details"),
    path("", index, name='index')
]
