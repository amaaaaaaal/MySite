from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
