# from django import forms 
from rest_framework import serializers 
from rest_framework.reverse import reverse
from .models import Product 
from . import validators


# like forms but serializers primarily to ease translation to json for api requests
# serializer no need to update the migrations, you can change fields as you like
# replaces model_to_dict to clean data for json communication
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) # this to specify name of my_discount
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title]) # runs functions in validators list when attempt to create; not sure if validators built-in or just kwarg
    # name = serializers.CharField(source='user.email', read_only=True) # source param indicates related existing field
    # url = serializers.SerializerMethodField(read_only=True) # not the ideal method to reference the product's own url
    url = serializers.HyperlinkedIdentityField( # hyperlink only works on a model serializer, whereas a serializer method field can be referenced anywhere else in class functions 
        view_name='product-detail', 
        lookup_field='pk'
    )
    # email = serializers.EmailField(write_only=True) # will only write to it, not read it
    class Meta:
        model = Product
        # must insert fields created above within this class, can also add fields from main model
        fields = [
            # 'user',
            'url',
            'edit_url',
            'id',
            'pk',
            # 'email',
            # 'name',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # # THIS BELOW IS A SIMPLE VALIDATION OF DATA EXAMPLE WITHIN THE SERIALIZER
    # def validate_title(self, value): # validate_<field_name> is std way to reference a field for validation
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value) # <field_name>__exact uses exact character matching when filtering the database
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product title")
    #     return value

    # # THIS COMMENTED OUT SINCE INCLUDED IN VIEWS.PY
    # def create(self, validated_data): # need this to prevent error bc cannot include write field in default serializer; validated_data is assuming the data is validated..
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email') # this to prevent error, since email is a write_only field
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj # don't need to save again, django saves automatically
    
    # # THIS COMMENTED OUT SINCE INCLUDED IN VIEWS.PY
    # def update(self, instance, validated_data): # django runs this update method if there is already an instance existing, otherwise runs create()
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return instance # don't need to save again, django saves automatically

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