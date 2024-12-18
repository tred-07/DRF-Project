from rest_framework import routers
from django.urls import include,path
from .views import RequestViewsets
router=routers.DefaultRouter()
router.register('r',RequestViewsets)

urlpatterns=[
    path('',include(router.urls)),
    # path('',RequestViewsets.as_view())
]