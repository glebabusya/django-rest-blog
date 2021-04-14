from django.urls import path
from . import views
urlpatterns = [
    path('', views.UsersListAPIView.as_view(), name='user_list'),
    path('<int:pk>', views.UserDetailAPIView.as_view(), name='user_detail'),
    path('registration', views.RegistrationAPIView.as_view(), name='registration'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('logout', views.LogoutAPIView.as_view(), name='logout')
]