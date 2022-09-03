
from rest_framework import serializers
from .models import *
import six
import uuid
from django.core.files.base import ContentFile
from rest_framework import status
from drf_extra_fields.fields import Base64ImageField


class Base64ImageField(serializers.ImageField):
	def to_internal_value(self, data):
		if isinstance(data, six.string_types):
			if "data:" in data and ";base64," in data:
				header, data = data.split(';base64,')
			try:
				decoded_file = base64.b64decode(data)
				print(decoded_file,':::::::::::::::::::::::::::::::::::::::::;')

			except TypeError:
				self.fail('invail_image')

			file_name = str(uuid.uuid4())#[:12]
			file_extension = "jpg"
			complate_file_name = "%s.%s" % (file_name, file_extension)
			
			data = ContentFile(decoded_file, complate_file_name)
			print('----------------------')
			
		return super(Base64ImageField, self).to_internal_value(data)


class EmployeeSerializer(serializers.ModelSerializer):
	photo= Base64ImageField(max_length=None, use_url=True)
	
	class Meta:
		model = Employee
		fields = '__all__'
	def create(self, valideted_data):
		img  = Employee()
		img.photo = valideted_data['photo']
		img.save()
		return img



