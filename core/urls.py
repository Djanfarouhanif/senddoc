from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('upload/<str:pk>', views.upload, name='upload'),
    path('docs', views.docs, name='docs'),
    
]