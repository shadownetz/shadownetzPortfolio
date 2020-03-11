from django.urls import path, include
from . import views

app_name = 'shadownetz_blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('developershub/', include('developershub.urls')),
    path('social-life/', include('sociallife.urls')),
    path('food/', include('food.urls'))

]