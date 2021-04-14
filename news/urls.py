from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post_list'),
    path('create', views.PostCreateAPIView.as_view(), name='post_create'),
    path('<int:pk>', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('comments/', include('comments.urls'))
]
