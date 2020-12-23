from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('accounts/', include("django.contrib.auth.urls")),
    path('', include("blog.urls")),
     path('weather', include("weather_api.urls")),
    path('admin/', admin.site.urls),
]
