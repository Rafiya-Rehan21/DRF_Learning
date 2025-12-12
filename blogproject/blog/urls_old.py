from django.urls import path
from . import views_old

urlpatterns = [
    # Function-based views
    path('fbv/posts/', views_old.post_list, name='fbv_post_list'),
    path('fbv/comments/', views_old.comment_list, name='fbv_comment_list'),

    # Class-based views
    path('cbv/posts/', views_old.PostListCreateAPIView.as_view(), name='cbv_post_list'),
    path('cbv/comments/', views_old.CommentListCreateAPIView.as_view(), name='cbv_comment_list'),
]
