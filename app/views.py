from rest_framework.viewsets import ModelViewSet

from app.models import User
from app.serializers import UserModelSerializer


class UserModelViewst(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
