from django.urls import path

from frontend.views import index, upload_photo, enhance_photo

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_photo, name='upload_photo'),
    path('enhance/', enhance_photo, name='enhance_photo'),
]