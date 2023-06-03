from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

"""
GET /produtos/: Lists all products.
POST /produtos/: Creates a new product.
"""
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

"""
GET /produtos/{id}/: Retrieves the details of a specific product.
PUT /produtos/{id}/: Updates a specific product.
PATCH /produtos/{id}/: Partially updates a specific product.
DELETE /produtos/{id}/: Deletes a specific product.
"""
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

"""
JSON format - GET/PUT/PATCH
{
  "name": "Nome do Produto",
  "price": 10,
  "category": "Categoria do Produto"
}
"""