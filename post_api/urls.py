from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='allPosts'),
    path('create', views.create, name='create'),
    path('<int:postId>', views.update, name='update'),
    path('post/<int:postId>', views.fetchPost, name='fetchPost'),
    path('<int:postId>/post', views.deletePost, name='delete')
]
