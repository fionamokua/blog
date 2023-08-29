
from django.urls import path
from .views import list_posts,post_detail,post_update,post_delete,PostDetail,PostList
# Create your views here.
urlpatterns=[
    path("apiview/",PostList.as_view(),name='get-post'),
    path("apiview/<int:pk>/",PostDetail.as_view(),name='get-post'),
   
    path('',list_posts,name='post-list'),
    path("<int:pk>/",post_detail,name='post-detail'),
    path("<int:pk>/update",post_update,name='post-update'),
    path("<int:pk>/delete/",post_delete,name='post-delete'),
]