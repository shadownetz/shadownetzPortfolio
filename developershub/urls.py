from django.urls import path
from . import views

app_name = "shadownetz_developershub"

urlpatterns = [
    path('', views.index, name="index")
]
