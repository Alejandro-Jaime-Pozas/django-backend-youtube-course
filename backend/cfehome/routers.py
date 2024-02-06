# TYPICALLY YOU'D PUT THE CODE IN ROUTERS.PY IN THE URLS.PY FOR MAIN PROJECT SETTINGS.PY FILE

from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
# router.register('products', ProductViewSet, basename='products') # register params: endpoint for url; 
router.register('products', ProductGenericViewSet, basename='products') # register params: endpoint for url; 
print(router.urls) # without printing no way to see what the actual urls included in DefaultRouter when registered are...
urlpatterns = router.urls 