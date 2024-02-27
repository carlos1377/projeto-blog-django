from django.urls import path
from django.conf import settings
from blog.views import index

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]
