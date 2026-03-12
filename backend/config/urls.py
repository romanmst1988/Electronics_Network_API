from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from network.views import NetworkNodeViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register("network", NetworkNodeViewSet)


urlpatterns = [

    path("admin/", admin.site.urls),

    path("api/", include(router.urls)),

    path("api/token/", TokenObtainPairView.as_view()),

    path("api/token/refresh/", TokenRefreshView.as_view()),

    path("api/schema/", SpectacularAPIView.as_view()),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema")
    ),
]