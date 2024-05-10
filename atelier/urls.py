from django.contrib import admin
from django.urls import path, include, reverse_lazy
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include("products.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),\
    path('', RedirectView.as_view(url=reverse_lazy('swagger-ui'), permanent=False)),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("config/", include("config.urls")),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
