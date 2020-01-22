import validators
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shortener.serializers import URLSerializer
from shortener.models import URLs
from shortener.shorten import get_short_id

@api_view(['POST'])
def shorten_url(request):
    if request.method == 'POST':
        try:
            url = request.data['url']
            if not url == '' and validators.url(url):
                short_id = get_short_id()
                url_obj, _ = URLs.objects.get_or_create(long_url=url,
                                                            defaults={
                                                                'pk' : short_id,
                                                                'short_url': settings.SITE_URL+short_id
                                                                })
                serializer = URLSerializer(url_obj)
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "URL not valid"}, status=400)
        except:
            return Response({"error": "bad request"} ,status=400)

def redirect_to_original_url(request, short_id):
    long_url_obj = get_object_or_404(URLs, pk=short_id, active=True)
    long_url_obj.count += 1
    long_url_obj.save()
    return HttpResponseRedirect(long_url_obj.long_url)