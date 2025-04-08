# serializers.py

from rest_framework import serializers
from news_app.models import News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


