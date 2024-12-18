from rest_framework import routers
from django.urls import include,path
from .views import ReviewViewsets
router=routers.DefaultRouter()
router.register('r',ReviewViewsets)

urlpatterns=[
    path('',include(router.urls)),
    # path('',RequestViewsets.as_view())
]