from django.urls import path
from main import  views

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('achieve',views.achieve,name='achievements')
]
