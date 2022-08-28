from . import views
from django.urls import path
 
 
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/<int:blog_post_id>/', views.PostDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('newPost/', views.newPost, name='newPost'),
]

#path('blog/create/', PostCreateView.as_view(), name='post_create'),
#path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
#path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

