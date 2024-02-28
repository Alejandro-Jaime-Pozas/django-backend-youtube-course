# this would normally go in a specific django app created for users
from rest_framework import serializers 

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', 
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

# if regular serializers.Serializer, don't need to include class: Meta, model or fields
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # THIS BELOW COMMENTED OUT BUT IS AN EXAMPLE OF HOW TO DO NESTED SERIALIZERS FOR EXAMPLE TO GET A USER'S PRODUCTS
    # other_products = serializers.SerializerMethodField(read_only=True)
    # insert other user data below

    # def get_other_products(self, obj):
    #     print(obj)
    #     user = obj 
    #     qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(qs, many=True, context=self.context).data # inserting the list of user products as qs into serializer; many=True allows for multiple iterations? not sure what .data does, maybe gets json type object which contains data which is the qs list itself