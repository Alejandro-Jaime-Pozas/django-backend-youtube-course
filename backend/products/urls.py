from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()), # always add end slashes in url path
    path('', views.ProductCreateAPIViews.as_view()),
]
