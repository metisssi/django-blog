from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Tady byla chyba, změněno z commit na urls
    path('', include('blog.urls')),
]