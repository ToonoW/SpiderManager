from rest_framework import viewsets, generics, filters

from backend import models
from backend import serializers


class ScrapydList(generics.ListCreateAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class ScrapydDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)

class ProjectDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class SpiderList(generics.ListCreateAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class SpiderDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer