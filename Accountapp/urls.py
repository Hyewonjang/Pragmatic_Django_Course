from django.urls import path

from Accountapp.views import hello_world

app_name = "Accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]