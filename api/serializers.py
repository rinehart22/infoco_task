from dataclasses import fields
from rest_framework import serializers
from .models import BlogPost, Task, item, srikanth, stud, woman, profile, man, upload
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
        #read_only_fields= ['pk']
        # if i want to validate some fields we can do here

    def validate_title(self, value):
        f = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            q =f.exclude(pk=self.instance.pk)
        if f.exists():
            raise serializers.ValidationError('title must be unique')
        return value


# it converts data to json
# do's validations for data passed

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'


class StudSerializer(serializers.ModelSerializer):

    class Meta:
        model = stud
        fields = ['skill']


class ManSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = man
        fields = ['url', 'id', 'game']


class womanSerializer(serializers.ModelSerializer):
    class Meta:
        model = woman
        fields = [field.name for field in model._meta.fields]
        fields = ['cook', 'symbol', 'price']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('id', 'verified')

    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])

    #     def random_with_N_digits(n):
    #         range_start = 10**(n-1)
    #         range_end = (10**n)-1
    #         return randint(range_start, range_end)

    #     otp = random_with_N_digits(6)
    #     user.otp = otp
    #     user.save()

    #     subject = 'Please Confirm Your Account'
    #     message = 'Your 6 Digit Verification Pin: {}'.format(otp)
    #     email_from = '*****'
    #     recipient_list = [str(user.email), ]
    #     send_mail(subject, message, email_from, recipient_list)
    #     return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = profile
        fields = '__all__'


class SrikanthSerializer(serializers.ModelSerializer):
    class Meta:
        model = srikanth
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = upload
        fields = '__all__'
