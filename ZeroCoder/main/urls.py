from django.urls import path, include
from . import views

urlpatterns = [
      path('', views.index, name='home'),
      path('new', views.new, name='new'),
      path('data', views.data, name='data'),
      path('test', views.test, name='test')
]
