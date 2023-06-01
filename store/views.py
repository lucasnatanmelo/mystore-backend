from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

"""
GET /categorias/: Lists all categories.
POST /categorias/: Creates a new category.
"""
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

"""
GET /categorias/{id}/: Retrieves the details of a specific category.
PUT /categorias/{id}/: Updates a specific category.
PATCH /categorias/{id}/: Partially updates a specific category.
DELETE /categorias/{id}/: Deletes a specific category.
"""
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

"""
GET /produtos/: Lists all products.
POST /produtos/: Creates a new product.
"""
class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


"""
GET /produtos/{id}/: Retrieves the details of a specific product.
PUT /produtos/{id}/: Updates a specific product.
PATCH /produtos/{id}/: Partially updates a specific product.
DELETE /produtos/{id}/: Deletes a specific product.
"""
class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
