
from rest_framework import serializers
from .models import *


from drf_extra_fields.fields import Base64ImageField

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class UploadSerializer(serializers.ModelSerializer):
	image= Base64ImageField()
	class Meta:
		model = Upload
		fields ='__all__'
