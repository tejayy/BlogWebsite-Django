from django.urls import path
from .views import HomeView, AddPostView, DeletePostView, ArticleDetailView, UpdatePostView

urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='atricle-detail'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='deletepost'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='updatepost'),
]