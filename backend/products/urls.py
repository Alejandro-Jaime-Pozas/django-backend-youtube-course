from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()), # always add end slashes in url path
    # path('', views.ProductCreateAPIViews.as_view()), # not using
    path('', views.ProductListCreateAPIViews.as_view()),
    path('<int:pk>/', views.product_alt_view), # testing with product_alt_view fn view
    path('', views.product_alt_view), # testing with product_alt_view fn view
]
