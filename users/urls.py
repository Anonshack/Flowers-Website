from django.urls import path
from .views import (
    RegistrationAPIView,
    LoginAPIView,
    Logout,
    AllUsers,
    UserDetailsView
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('all-users/', AllUsers.as_view(), name='all-users'),
    path('user-detail/<int:pk>/', UserDetailsView.as_view(), name='user-detail'),
    path('logout/', Logout.as_view(), name='logout'),
]
