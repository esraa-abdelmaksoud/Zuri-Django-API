from django.shortcuts import render
from .models import Link
from .serializers import LinkSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.
class LinkListAPI(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkUpdateApi(generics.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class LinkDeleteApi(generics.DestroyAPIView):
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer