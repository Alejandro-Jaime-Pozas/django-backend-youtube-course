# from django import forms 
from rest_framework import serializers 

from .models import Product 


# like forms but serializers primarily to ease translation to json for api requests
# replaces model_to_dict to clean data for json communication
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) # this to specify name of my_discount
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    # this to change display name of get_discount() Product model function
    def get_my_discount(self, obj): # obj is the actual INSTANCE of the class being called
        # print(obj.id)
        if not hasattr(obj, 'id'): # 2 ways of checking if instance of class exists
            return None 
        if not isinstance(obj, Product): # 2 ways of checking if instance of class exists
            return None 
        return obj.get_discount()



# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#         ]