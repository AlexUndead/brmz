from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
    path('legitimacy_activities/', views.legitimacy_activities, name='legitimacy_activities'),
    path('download_catalog/', views.download_catalog, name='download_catalog'),
    path('news/', views.news, name='news'),
    path('', views.index, name='index'),
]
