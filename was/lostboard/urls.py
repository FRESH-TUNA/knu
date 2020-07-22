from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# 분실물 urls.py
app_name = 'lostboard'
urlpatterns = [
    path('find', views.find, name="find"),
    path('lost', views.lost, name="lost"),
    path('createpost/', views.createpost, name="createpost"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/createcomment/', views.createcomment, name="createcomment"),
    path('<int:pk>/deletepost/', views.deletepost, name="deletepost"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)