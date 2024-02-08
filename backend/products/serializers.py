# from django import forms 
from rest_framework import serializers 
from rest_framework.reverse import reverse
from .models import Product 


# like forms but serializers primarily to ease translation to json for api requests
# replaces model_to_dict to clean data for json communication
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) # this to specify name of my_discount
    edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True) # not the ideal method to reference the product's own url
    url = serializers.HyperlinkedIdentityField( # hyperlink only works on a model serializer, whereas a serializer method field can be referenced anywhere else in class functions 
        view_name='product-detail', 
        lookup_field='pk'
    )
    email = serializers.EmailField(write_only=True) # will only write to it, not read it
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'email',
            'id',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def create(self, validated_data): # need this to prevent error bc cannot include write field in default serializer; validated_data is assuming the data is validated..
        # return Product.objects.create(**validated_data)
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        print(email, validated_data)
        return obj

    def get_edit_url(self, obj): # seems like get_<field_name> is the syntax used to refer to a serializer read_only field that is not in the original db model
        request = self.context.get('request') # can't directly do self.request since serializers don't always have a request, depends on context
        if request is None: 
            return None 
        return reverse(viewname='product-edit', kwargs={'pk': obj.pk}, request=request) # different from default django reverse(), this is from rest_framework
        # return f"/api/products/{obj.pk}/" # NOT IDEAL SINCE IF YOU CHANGE API URL, HAVE TO MANUALLY UPDATE
    
    # this to change display name of get_discount() Product model function
    def get_my_discount(self, obj): # obj is the actual INSTANCE of the class being called
        # print(obj.id)
        if not hasattr(obj, 'id'): # 2 ways of checking if instance of class exists
            return None 
        if not isinstance(obj, Product): # 2 ways of checking if instance of class exists
            return None 
        return obj.get_discount()


# # forms.modelForm similar to zerializes in how they are constructed
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#         ]