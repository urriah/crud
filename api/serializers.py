from rest_framework.serializers import ModelSerializer
from .models import Build


class BuildSerializer(ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'