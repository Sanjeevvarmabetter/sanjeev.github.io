from . import views
from django.urls import path
from .views import members
urlpatterns = [
    path('',members.as_view(), name='frontpage'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]


