from django.urls import path

from frontend.views import index

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_photo, name='upload_photo'),
]