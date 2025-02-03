from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_results/', views.main_search, name='main_search')
]