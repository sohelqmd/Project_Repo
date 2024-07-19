from rest_framework import serializers
from .models import ItInstitute,ItContactInformation

class ItInstituteSerializer(serializers.ModelSerializer):
  class Meta:
    model = ItInstitute
    fields = "__all__"

class ItContactInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = ItContactInformation
    fields = "__all__"