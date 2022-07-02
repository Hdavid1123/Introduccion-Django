from django.urls import path
from .view import BlogListView

app_name='blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home')
]