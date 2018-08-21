from django.urls import path

from . import views

urlpatterns = [
    path('pages/<int:page_id>/', views.sample, name = 'page'),
]
