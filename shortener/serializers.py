from rest_framework import serializers
from shortener.models import URLs

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLs
        fields = '__all__'