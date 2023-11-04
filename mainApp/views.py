from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class YangilikModelViewSet(ModelViewSet):
    queryset = Yangilik.objects.order_by('-vaqt')
    serializer_class = YangilikSerializer


class XodimModelViewSet(ModelViewSet):
    queryset = Xodim.objects.all()
    serializer_class = XodimSerializer


class XizmatModelViewSet(ModelViewSet):
    queryset = Xizmat.objects.all()
    serializer_class = XizmatSerializer


class IchimlikModelViewSet(ModelViewSet):
    queryset = Ichimlik.objects.all()
    serializer_class = IchimlikSerializer


class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer


