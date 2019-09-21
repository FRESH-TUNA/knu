from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# 총학문의게시판 urls.py
app_name = 'qnaknuch'
urlpatterns = [
    path('', views.board, name="board"),
    path('createpost/', views.createpost, name="createpost"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/createcomment/', views.createcomment, name="createcomment"),
    path('<int:pk>/deletepost/', views.deletepost, name="deletepost"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)