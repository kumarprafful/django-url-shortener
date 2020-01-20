from django.urls import path
from shortener.views import shorten_url, redirect_to_original_url

urlpatterns = [
    path('shorten/',shorten_url,name="shorten"),
    path('<short_id>', redirect_to_original_url, name="redirect_original"),
]