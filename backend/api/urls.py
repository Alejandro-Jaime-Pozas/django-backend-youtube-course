# created this file manually to separate urls for this api app
from django.urls import path , include

from . import views 


urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    # path('products/', include('products.urls')), # could potentially do this to include all api functionality in just one file
]
