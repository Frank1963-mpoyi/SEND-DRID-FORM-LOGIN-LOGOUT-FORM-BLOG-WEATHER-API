from django.urls import path, include
from weather_api import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()# create variable to store default router
router.register('descriptions', views.DescriptionViewSet) #call the register method on the router
urlpatterns = [
    
    path('', include(router.urls))# django will search url pattern in this location
    
]
