from rest_framework import routers  
from .views import ListViewSet, ItemViewSet


api_router = routers.SimpleRouter()  
api_router.register('lists', ListViewSet) 
api_router.register('items', ItemViewSet)