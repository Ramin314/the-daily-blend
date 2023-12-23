from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feeds/', views.feeds, name='feeds'),
    path('feeds/<uuid:feed_id>/', views.feed, name='feed'),
    path('stories/', views.stories, name='stories'),
    path('stories/<uuid:story_id>/', views.story, name='story'),
    path('topics/', views.topics, name='topics'),
    path('topics/<uuid:topic_id>/', views.topic, name='topic'),
]
