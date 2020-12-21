from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^fotografia/', views.post_foto, name='post_foto'),
    url(r'^musica/', views.post_musica, name='post_musica'),
]
