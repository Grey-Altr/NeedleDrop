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
    # Detail path
    path(
        'releases/<int:pk>/',
        views.ReleaseDetail.as_view(),
        name='release-detail',
    ),
    # Create path
    path(
        'releases/create/',
        views.ReleaseCreate.as_view(),
        name='release-create',
    ),
    # Update path
    path(
        'releases/<int:pk>/update/',
        views.ReleaseUpdate.as_view(),
        name='release-update',
    ),
    # Delete path
    path(
        'releases/<int:pk>/delete/',
        views.ReleaseDelete.as_view(),
        name='release-delete',
    ),
    # Auth/signup path
    path(
        'accounts/signup/',
        views.signup,
        name='signup',
    ),
]