from rest_framework import generics 

from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer