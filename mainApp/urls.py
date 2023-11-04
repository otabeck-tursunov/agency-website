from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .views import *


schema_view = get_schema_view(
    openapi.Info(
        title="Agency Website API Documentation",
        default_version="v1",
        description="Ichimlik - Mijoz uchun tavsiya qatoridagi ichimliklar! \n"
                    "Xodim - Bizning Jamoa qismidagi har bir a'zo ma'lumoti! \n"
                    "Xizmat - Xizmat ko'rsatish turlari! \n"
                    "Mijoz - qiziqish so'rovini bildirgan mijozlar ma'lumoti!",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="tursunovotabekkuva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # include_schema = True,
)


r_yangilik = DefaultRouter()
r_yangilik.register(r'', YangilikModelViewSet)

r_xodim = DefaultRouter()
r_xodim.register(r'', XodimModelViewSet)

r_xizmat = DefaultRouter()
r_xizmat.register(r'', XizmatModelViewSet)

r_ichimlik = DefaultRouter()
r_ichimlik.register(r'', IchimlikModelViewSet)

r_mijoz = DefaultRouter()
r_mijoz.register(r'', MijozModelViewSet)


urlpatterns = [
    path('yangilik/', include(r_yangilik.urls)),
    path('xodim/', include(r_xodim.urls)),
    path('xizmat/', include(r_xizmat.urls)),
    path('ichimlik/', include(r_ichimlik.urls)),
    path('mijoz/', include(r_mijoz.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
