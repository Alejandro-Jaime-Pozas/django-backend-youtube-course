from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIViews.as_view(), name='product-list'),# naming convention for name param is the <model_name>-list for the list views;
    # path('', views.ProductCreateAPIViews.as_view()), # not using
    # path('', views.ProductMixinView.as_view()), # not using; for mixins
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'), # naming convention for name param is the <model_name>-detail for the detail views;
    # path('<int:pk>/', views.ProductMixinView.as_view()), # always add end slashes in url path
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    # path('<int:pk>/', views.product_alt_view), # testing with product_alt_view fn view
    # path('', views.product_alt_view), # testing with product_alt_view fn view
]
