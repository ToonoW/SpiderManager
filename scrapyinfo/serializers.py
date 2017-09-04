from rest_framework import serializers
from scrapyinfo import models


class ScrapydSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Scrapyd
        fields = ('id', 'name', 'ip', 'port', 'comment')


class ProjectSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=45, read_only=True)

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'scrapyd', 'comment')


class SpiderSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=45, read_only=True)

    class Meta:
        model = models.Spider
        fields = ('id', 'name', 'project', 'comment')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = ('id', 'name', 'spiders', 'comment')
