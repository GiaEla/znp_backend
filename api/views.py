from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

from api.serializers import EventSerializer
from api.models import Event


class EventApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, event_id, format=None):
        event = Event.objects.get(id=event_id)
        event_serializer = EventSerializer(event)

        return Response(event_serializer.data, status=status.HTTP_200_OK)


    def put(self, request, event_id, format=None):

        event = Event.objects.get(id=event_id)

        event_serializer = EventSerializer(event, data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response('')

        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventListApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        today = datetime.datetime.today()
        event_list = Event.objects.filter(start_date__gte=today)
        event_list_serializer = EventSerializer(event_list, many=True)

        return Response(event_list_serializer.data, status=status.HTTP_200_OK)