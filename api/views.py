from django.http import JsonResponse
from .models import Country, State
from .serializers import CountrySerializer, StateSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# def country_list(request):
#     # countries = [{'code':'US', 'name':'United States'}, {'code':'CA','name':'Canada'}, {'code':'AU','name':'Australia'}]
#     countries = Country.objects.all()
#     serializer = CountrySerializer(countries, many=True)
#     return JsonResponse(serializer.data, safe=False)

class CountryList(APIView):
    def get(request, format=None):
        countries = Country.objects.all()
        country_serializer = CountrySerializer(countries, many=True)
        return Response(country_serializer.data)

class StateList(APIView):
    def get(request, format=None, **kwargs):
        current_country = Country.objects.filter(code=kwargs['country_code'])
        states = State.objects.filter(country=current_country)
        state_serializer = StateSerializer(states, many=True)
        return Response(state_serializer.data)