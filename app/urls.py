from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feeds/', views.feeds, name='feeds'),
    path('feeds/<uuid:feed_id>/', views.feed, name='feed'),
]
