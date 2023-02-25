from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import UserModelViewst
#
router = DefaultRouter()
router.register('', UserModelViewst)

urlpatterns = [
    path('',include(router.urls))
]