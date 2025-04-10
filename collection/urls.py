from django.urls import path
from . import views

urlpatterns = [
    # Home path
    path(
        '',
        views.Home.as_view(),
        name='home',
    ),
    # Release Index path
    path(
        'releases/',
        views.ReleaseList.as_view(),
        name='release-index',
    ),
    # Auth/signup path
    path(
        'accounts/signup/',
        views.signup,
        name='signup',
    ),
]