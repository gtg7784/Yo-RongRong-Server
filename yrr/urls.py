from django.conf.urls import url

from . import views

urlpatterns = [
    url('compare/', views.getResult),
    url('getall/', views.getAllProducts)
]
