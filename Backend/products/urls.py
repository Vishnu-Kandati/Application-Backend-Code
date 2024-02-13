from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import detail_view, create_user
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version='v1',
        description="Products description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('items/', detail_view, {'model_cls': Item, 'serializer_cls': ItemSerializer}, name='item-list'),
    path('items/<str:sku>/', detail_view, {'model_cls': Item, 'serializer_cls': ItemSerializer}, name='item-detail'),
    path('categories/', detail_view, {'model_cls': Category, 'serializer_cls': CategorySerializer}, name='category-list'),
    path('create_user/', create_user, name='create_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]