from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_index, name = "page_index"),
    path("<int:pk>/", views.page_detail, name = "page_detail"),
]