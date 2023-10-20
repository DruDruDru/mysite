from django.urls import path

from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('sighup/', views.SighUpView.as_view(), name='sighup'),
    path('edit/<int:pk>', views.CustomUserUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.CustomUserDelete.as_view(), name='delete_user_confirm'),
]
