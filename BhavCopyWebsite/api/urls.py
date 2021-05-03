from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import search, scrip

urlpatterns = {
    path('search', search, name="search"),
    path('scrip/<str:scrip_name>', scrip, name="scrip")
}

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
