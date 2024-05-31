from django.urls import path

from blog.views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_active

app_name = 'blog'

urlpatterns = [
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('blog_create', BlogCreateView.as_view(), name='blog_create'),
    path('blog_edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity/<int:pk>', toggle_active, name='toggle_active'),
]
