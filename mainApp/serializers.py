from rest_framework import serializers
from .models import Yangilik, Xodim, Xizmat, Ichimlik, Mijoz


class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = "__all__"


class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = "__all__"


class XizmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmat
        fields = '__all__'


class IchimlikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ichimlik
        fields = '__all__'


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
