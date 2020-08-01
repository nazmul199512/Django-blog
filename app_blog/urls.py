from django.urls import path
from . import views 

app_name = 'app_blog'

urlpatterns = [
    path('',views.blog_list.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unlike, name='unliked'),
    path('my_blog/', views.myBlog.as_view(), name='my_blog'),
    path('update_blog/<pk>/', views.UpdateBlog.as_view(), name='update_blog'),
]
