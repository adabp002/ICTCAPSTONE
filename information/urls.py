from django.urls import path
from . import views

urlpatterns = [
    path('user-guide/', views.info_view, name='user-guide'),
    path('about-us/', views.about_us, name='about-us'),
]
