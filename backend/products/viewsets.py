# TYPICALLY YOU'D PUT VIEWSETS IN THE VIEWS.PY FILE

from rest_framework import mixins, viewsets 

from .models import Product 
from .serializers import ProductSerializer


# VIEWSETS ALLOW YOU TO ACCEPT ALL METHODS WITH VERY LIMITED CODE, BUT THE URL ENDPOINTS ARE DETERMINTED BY DEFAULT BY THE VIEWSET CONFIGURATION. BEST TO CREATE YOUR OWN VIEWS AND URL ENDPOINTS FOR EACH? UNLESS CREATING A SIMPLE APP MAYBE VIEWSETS ARE BETTER. 
class ProductViewSet(viewsets.ModelViewSet):
    '''
    get >> list >> Queryset
    get >> retrieve >> Product Instance Detail View
    post >> create >> New Instance
    put >> update
    patch >> partial update
    delete >> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get >> list >> Queryset
    get >> retrieve >> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default

# THIS BELOW NEEDED TO SPECIFY NAMING CONVENTION FOR DIFFERENT URL ENDPOINTS FOR VIEWSET
product_list = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})