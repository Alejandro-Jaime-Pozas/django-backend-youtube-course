from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# CREATE VIEW CREATES A MODEL INSTANCE & SERIALIZER INSTANCE
class ProductCreateAPIViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

    # specific method for CreateAPIView
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user) # if have user, to create serializer instance
        # print(serializer.validated_data) # prints the validated data inputs
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None 
        if not content:
            content = title 
        serializer.save(content=content)
        # serializer.save()
        # can also send a Django signal

# DETAIL VIEW GETS ONE SINGLE ITEM
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # serializer_class is installed package in rest_framework
    # lookup_field = 'pk'

    # # to get a custom queryset 
    # def def get_queryset(self):
    #     return super().get_queryset()
    