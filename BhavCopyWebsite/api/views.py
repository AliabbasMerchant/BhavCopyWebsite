from typing import Optional, Any, Dict
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response

redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


def get_scrip_details(scrip_name: str) -> Optional[Dict[str, Any]]:
    scrip_details = redis_instance.hgetall(scrip_name)
    if scrip_details != {}:
        details = {
            key.decode('utf-8'): scrip_details[key].decode('utf-8') for key in scrip_details
        }
        details['name'] = scrip_name
        return details
    return None


@api_view(['GET'])
def search(request, *args, **kwargs):
    search_string: str = request.GET.get('q', '')
    search_string = search_string.upper()

    matching_scrip_names = redis_instance.keys(f"*{search_string}*")

    search_results = []
    for scrip_name in matching_scrip_names:
        scrip_name = scrip_name.decode('utf-8')
        scrip_details = get_scrip_details(scrip_name)
        if scrip_details is not None:  # would never be None, as we are sure that the scrip_name exists
            search_results.append(scrip_details)

    return Response(search_results, status=200)


@api_view(['GET'])
def scrip(request, scrip_name: str, *args, **kwargs):
    scrip_name = scrip_name.upper()
    scrip_details = get_scrip_details(scrip_name)
    if scrip_details is not None:
        return Response(scrip_details, status=200)

    return Response({'msg': 'Not found'}, status=404)
