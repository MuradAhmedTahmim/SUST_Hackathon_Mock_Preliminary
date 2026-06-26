from django.urls import path
from .views import health, sort_ticket

urlpatterns = [
    path("health", health),
    path("health/", health),
    path("sort-ticket", sort_ticket),
    path("sort-ticket/", sort_ticket),
]
