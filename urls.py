from rest_framework.routers import DefaultRouter, SimpleRouter

from django.conf import settings
from django.urls import include, path

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# Register your viewsets here

urlpatterns = [
    # Include the rest of the urls here
    path("", include(router.urls)),
]
