from django.urls import path
from . import views

urlpatterns = [
    # Home path
    path(
        '',
        views.home,
        name='home',
    ),
]