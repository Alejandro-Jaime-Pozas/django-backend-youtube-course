import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view 
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs): # the request param is a django httprequest instance
    data = request.data # seems to get the body content of request..
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True): # if fields from request match those required by ProductSerializer
        # instance = serializer.save() # need to save to create an instance of class
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': "not good data"}, status=400)



# # fn view to get data
# @api_view(["GET"])
# def api_home(request, *args, **kwargs): # the request param is a django httprequest instance
#     """
#     DJANGO REST FRAMEWORK API VIEW
#     """
#     # print(request.__dict__)
#     instance = Product.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)



# # OLD WAY USING model_to_dict
# @api_view(["GET"])
# def api_home(request, *args, **kwargs): # the request param is a django httprequest instance
#     """
#     DJANGO REST FRAMEWORK API VIEW
#     """
#     print(request.__dict__)
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#     return Response(data)