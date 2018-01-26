from rest_framework import generics, filters

from public.views import APIView
from scrapyinfo import models
from scrapyinfo import serializers
from scrapyinfo.utils import scrapyinfo as scrapyinfo_utils


class RefreshPlatformView(APIView):
    """
    刷新平台信息API
    """

    def get(self, _):
        try:
            scrapyinfo_utils.refresh_all_project_and_scrapy()
            self.status = True
        except:
            self.status = False
            self.msg = '刷新所有信息未能成功'
        finally:
            return self.json_response()


"""
使用Django RESTful Framework编写的

对数据模型进行增删改查的API
"""


class ScrapydList(generics.ListCreateAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer
    filter_fields = ('id', 'name',)


class ScrapydDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer


class ProjectList(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_fields = ('id', 'name',)


class ProjectDetial(generics.RetrieveUpdateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class SpiderList(generics.ListAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer
    filter_fields = ('id', 'name', 'project',)


class SpiderDetial(generics.RetrieveUpdateAPIView):
    queryset = models.Spider.objects.all()
    serializer_class = serializers.SpiderSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_fields = ('id', 'name', 'spiders')


class GroupDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
