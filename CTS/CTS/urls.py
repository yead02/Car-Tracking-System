from django.contrib import admin
from django.urls import path, re_path, include
from OperatorApp import views as OV
from ManagerApp import views as MV
from CityApp import views as CV
from CarApp import views as CAV
from ReportApp import views as RV
from TrackingApp import views as TV
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('operatorinfo', OV.OperatorMVS, basename='operators')
router.register('managerinfo', MV.ManagerMVS, basename='managers')
router.register('cityinfo', CV.CityMVS, basename='cities')
router.register('carinfo', CAV.CarMVS, basename='cars')
router.register('reportinfo', RV.ReportMVS, basename='reports')
router.register('trackinginfo', TV.TrackingMVS, basename='trackings')

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('opeinfo/', OV.OperatorLC.as_view()),
    # path('opeinfo/<int:pk>', OV.OperatorRUD.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
