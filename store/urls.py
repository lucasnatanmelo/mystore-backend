from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view()),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view()),
    path('produtos/', views.ProdutoList.as_view()),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view()),
]
