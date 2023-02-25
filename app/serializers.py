from rest_framework.serializers import ModelSerializer

from app.models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ()