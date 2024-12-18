from django.urls import include,path
from rest_framework import routers
from .views import AdvertiseViewsets

router=routers.DefaultRouter()
router.register('advertise',AdvertiseViewsets)

urlpatterns=[
    path('',include(router.urls)),
    # path('advertise/',AdvertiseViewsets.as_view(),name='advertise')
]