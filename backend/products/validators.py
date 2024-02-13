from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product 


# # can validate if a unique object already exists in db
# def validate_title(value): # validate_<field_name> is std way to reference a field for validation
#     qs = Product.objects.filter(title__iexact=value) # <field_name>__exact uses exact character matching when filtering the database
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} is already a product title")
#     return value

def validate_title_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")



unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')