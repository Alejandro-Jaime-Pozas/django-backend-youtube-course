from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404

from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermission

# MIXINS are a great way to shortcut having to manually copy paste same code into different views

# GET, POST: LIST CREATE VIEW NOT ONLY LISTS ALL INSTANCES STORED IN DATABASE, ALSO CREATES A MODEL INSTANCE & SERIALIZER INSTANCE
class ProductListCreateAPIViews(
    StaffEditorPermissionMixin, # this mixin allows us to set default permission classes w/o need to set permission_classes within class
    UserQuerySetMixin, # gets the current user instance to narrow down query base
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # allow_staff_view = True  # you can change your own mixin variables for specific views
    # user_field = 'owner' # testing here if mixin works, should throw error
    # # FOR AUTHENTICATION AND PERMISSIONS - DONT NEED THIS IF USING GLOBAL SETTINGS.PY DEFAULT AUTH/PERMISSIONS FOR REST_FRAMEWORK
    # authentication_classes = [
    #     authentication.SessionAuthentication, # prob identifies a live session based on local storage or some time variable
    #     TokenAuthentication, # to require user token
    # ] # prob checks for a token non expired
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # order matters, first make sure user is admin user, then give the user the custom staff editor permission
    # permission_classes = [permissions.DjangoModelPermissions] # to include default permissions for users (which defaults to no permissions)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # with read only option, it allows for get method but not the other methods

    # specific method for CreateAPIView
    def perform_create(self, serializer): # this not often the preferred way of modifying create fn
        # serializer.save(user=self.request.user) # if have user, to create serializer instance
        # print(serializer.validated_data) # prints the validated data inputs
        if serializer.validated_data.get('email'):
            email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None 
        if not content:
            content = title 
        serializer.save(user=self.request.user, content=content) # like commit() in flask; why need to specify content=content?
        # serializer.save()
        # can also send a Django signal ie look into signals

    # # THIS BELOW IS IN MIXINS.PY IN MAIN API FOLDER
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs) # returns the queryset for this view
    #     request = self.request
    #     user = request.user 
    #     if not user.is_authenticated:
    #         return Product.objects.none() # return empty list related to model
    #     # print(request.user)
    #     return qs.filter(user=request.user) # checking here that the user attr in Product model = request.user

# CREATE VIEW CREATES A MODEL INSTANCE & SERIALIZER INSTANCE
class ProductCreateAPIViews(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

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
class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # serializer_class is installed package in rest_framework
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # lookup_field = 'pk'
    # # to get a custom queryset 
    # def def get_queryset(self):
    #     return super().get_queryset()

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # serializer_class is installed package in rest_framework
    lookup_field = 'pk' # lookup_field included in UpdateAPIView
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    # 
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 
            ###


class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # serializer_class is installed package in rest_framework
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_destroy(self, instance): # destroy inputs the instance itself, not the serializer
        # instance
        super().perform_destroy(instance) # this is the code that performs the instance delete

# # NOT GOING TO USE THIS METHOD
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# mixin views allow for access to additional methods built-in to mixins that are otherwise unavailable
class ProductMixinView(
    mixins.ListModelMixin, # for handling get list
    mixins.RetrieveModelMixin, # for handling get 1 item
    mixins.CreateModelMixin, # for creating 1 item
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # the ListModelMixin doesn't use this field

    # for mixins, you can change this from get to post and still works
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs) # will change what this mixin responds with (retrieve is a RetrieveModelMixin method)
        return self.list(request, *args, **kwargs) # this list method comes directly from ListModelMixin

    def post(self, request, *args, **kwargs): #http >> POST
        return self.create(request, *args, **kwargs)


# create fn view that does entire CRUD within this one view (for learning purposes only)
# this view is confusing, purpose is to see logic behind the django classes
# function based views are a lot more flexible, but more code/confusion
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 
    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk) # will return not found error if not in db
            data = ProductSerializer(obj, many=False).data 
            return Response(data)
        # list view
        qs = Product.objects.all() # queryset
        data = ProductSerializer(qs, many=True).data 
        return Response(data)
    
    if method == 'POST':
        # create view: create an instance
        serializer = ProductSerializer(data=request.data) # not sure where 'data' field is in ProductSerializer class...
        if serializer.is_valid(raise_exception=True): # if fields from request match those required by ProductSerializer
            # instance = serializer.save() # need to save to create an instance of class
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None 
            if not content:
                content = title 
            serializer.save(content=content) # not sure why only specifying content and NOT title here...
            return Response(serializer.data)
        return Response({'invalid': "not good data"}, status=400)