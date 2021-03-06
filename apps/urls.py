from django.urls import path

from apps.others import views

urlpatterns = [
    path("index", views.index)
]