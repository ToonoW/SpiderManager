from rest_framework import viewsets, generics, filters

from scrapyinfo import models
from scrapyinfo import serializers


def refresh_platform_information(request):
    pass


"""
使用Django RESTful Framework编写的

对数据模型进行增删改查的API
"""

class ScrapydList(generics.ListCreateAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class ScrapydDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer


class ProjectList(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)

class ProjectDetial(generics.RetrieveUpdateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class SpiderList(generics.ListAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class SpiderDetial(generics.RetrieveUpdateAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'spider')


class GroupDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

