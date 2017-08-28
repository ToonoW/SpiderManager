from rest_framework import serializers
from backend.models import Scrapyd


class ScrapydSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scrapyd
        fields = ('id', 'name', 'ip', 'port', 'comment')