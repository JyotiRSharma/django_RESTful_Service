from rest_framework import serializers
from .models import Stock

# This class transform Stock model to JSON format(Serialize)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        # fiels = ('ticker', 'volume')
        fields = '__all__'

