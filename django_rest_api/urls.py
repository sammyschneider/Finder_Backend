
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foods_api.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
