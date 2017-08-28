from rest_framework import viewsets, generics, filters

from backend import models
from backend import serializers


class ScrapydList(generics.ListCreateAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id', 'name',)


class ScrapydDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Scrapyd.objects.all()
    serializer_class = serializers.ScrapydSerializer