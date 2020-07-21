from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='selfteach-home'),
    path('readme/', views.readme, name='readme'),
    path('booksummary/', views.booksummary_view, name='booksummary'),
]