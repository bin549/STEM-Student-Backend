from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('users.urls')),
    path('api/', include('course.urls')),
    path('api/', include('homework.urls')),
]
