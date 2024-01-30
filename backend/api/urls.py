# created this file manually to separate urls for this api app
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token # use for endpoint in api to create auth tokens

from . import views 


urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    path('auth/', obtain_auth_token), # obtain_auth_token is a hidden view
    # path('products/', include('products.urls')), # could potentially do this to include all api functionality in just one file
]
