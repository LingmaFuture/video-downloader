from django.contrib import admin
from django.urls import path
from .views import index,download_file

urlpatterns = [
    path('', index),
    path('download/', download_file, name='download_file'),  # 添加下载路径
]