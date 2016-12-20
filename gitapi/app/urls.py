from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teste/$', views.teste, name='teste'),
    url(r'^perfil/', views.perfil, name='perfil'),
]