from django.urls import path
from . import views

urlpatterns = [
    # Home path
    path(
        '',
        views.Home.as_view(),
        name='home',
    ),
]