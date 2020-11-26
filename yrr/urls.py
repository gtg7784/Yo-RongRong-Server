from django.conf.urls import url

from . import views

urlpatterns = [
    url('/', views.index, name='index'),
    url('compare/', views.getResult),
    url('getall/', views.getAllProducts)
]
