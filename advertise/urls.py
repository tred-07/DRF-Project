from django.urls import path,include
from rest_framework import routers
from .views import AdvertiseViewset
router=routers.DefaultRouter()

router.register('advertise',AdvertiseViewset)

urlpatterns=[
    path('',include(router.urls))
]
