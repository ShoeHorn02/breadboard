from django.urls import path
from .views import BoardPost

app_name = 'blog_api'

urlpatterns = [
    path('boardpost', BoardPost.as_view(), name='boardpost'),
]
