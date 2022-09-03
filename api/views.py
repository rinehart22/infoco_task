from rest_framework import serializers
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from .serializers import LoginSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework.exceptions import NotFound
from rest_framework import mixins
from rest_framework.parsers import JSONParser, FileUploadParser
from cgitb import lookup
from msilib import schema
from multiprocessing import AuthenticationError
from pydoc import allmethods
from re import A
from urllib import response
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.http import JsonResponse
from matplotlib.font_manager import json_dump, json_load
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import BlogPost, Task, item, stud, woman, man, upload, srikanth
from api import serializers
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework import status
# from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, mixins
import requests
from django.db.models import Q


class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # or ListCreateAPIView
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        q = BlogPost.objects.all()
        qs = self.request.GET.get('t')
        if qs is not None:
            qr = q.filter(Q(title__icontains=qs) | Q(
                content__icontains=qs)).distinct()
        return q

    # def post(self, serializer):                 # without this also we can create, list without mixins
        # serializer.save(user=self.request.user)

    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    # pass
    #lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk)


# txt = "The list in Spain"
# x = re.search('list', txt)


# The @api_view decorator for working with function based views.

# The APIView class for working with class-based views.


class LoginView(APIView):

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        serilaizer = UserSerializer(items, many=True)
        url = "https://www.fast2sms.com/dev/bulkV2"
        print('----------')
        querystring = {"authorization": "urd4LAPM1zKqFEl3DhRtOYiswmcSoeJabU6CXgx9vjfQV0HI87c8Ju3Cwytsx4pSkiXMENPQKGfVevhl",
                       "variables_values": "559945", "route": "otp", "numbers": "9494196374"}

        headers = {'cache-control': "no-cache"}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        return Response(usernames)

    def post(self, request, format=None):
        data = request.data
        print('--------------------------')
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.two_step_verification:

                    # GENERATE OTP HERE AND SAVE THIS IN USER MODEL...
                    url = "https://www.fast2sms.com/dev/bulkV2"

                    querystring = {"authorization": "urd4LAPM1zKqFEl3DhRtOYiswmcSoeJabU6CXgx9vjfQV0HI87c8Ju3Cwytsx4pSkiXMENPQKGfVevhl",
                                   "variables_values": "559945", "route": "otp", "numbers": "9494196374"}

                    headers = {'cache-control': "no-cache"}

                    response = requests.request(
                        "GET", url, headers=headers, params=querystring)
                    user.otp = response
                    print(response, '-----------------')
                    user.save(update_fields=['otp', ])

                    return Response({"send": "Two step verification OTP successfully send!!!"}, status=status.HTTP_200_OK)
            else:
                return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def apioverview(request):
    permission_classes = (IsAuthenticated,)
    api_url = {
        'list': 'list',
        'create': 'creat',
        'del': 'delete',
        'up': 'update',

    }

    return Response(api_url)

    # safe to False. If we did not set this parameter, we would get a TypeError with the following message:

    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    # By default, JsonResponse accepts only Python dictionaries.


# If the safe parameter is set to False , any object can be passed for serialization; otherwise only dict instances are allowed

# class verifyOTPView(APIView):

#     def post(self, request):
#         username = request.data["username"]
#         otp = int(request.data["otp"])
#         user = User.objects.get(username=username)
#         if int(user.otp)==otp:
#             user.verified = True
#             #user.otp.delete()  #?? How to handle the otp, Should I set it to null??
#             user.save()
#             return Response("Verification Successful")
#         else:
#             raise PermissionDenied("OTP Verification failed")


# Class ValidatePhoneSendOTPView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request, *args, **kwargs):
#         name = request.data.get('name' , False)
#         phone_number = request.data.get('phone')
#         if phone_number:
#             phone  = str(phone_number)
#             user = User.objects.filter(phone__iexact = phone)

#             if user.exists():
#                 return Response({
#                     'status' : False,
#                     'detail' : 'Phone number already exists.'
#                     })
#             else:
#                 key = send_otp(phone)

#                 if key:
#                     old = Customer.objects.filter(phone__iexact = phone)
#                     if old.exists():
#                         old  = old.first()
#                         count = old.count
#                         # if count > 20:
#                         #     return Response({
#                         #         'status': False,
#                         #         'detail' : 'Sending otp error. Limit Exceeded. Please contact customer support.'
#                         #         })
#                         old.count = count + 1
#                         old.save()
#                         print('Count Increase', count)
#                         return Response({
    #                     'status' : True,
    #                     'detail' : 'OTP sent successfully.'
    #                     })
    #             else:
    #                 PhoneOTP.objects.create(
    #                     # name = name,
    #                     phone = phone,
    #                     otp = key,

    #                     )
    #                 link = f'API-urls'
    #                 requests.get(link)
    #                 return Response({
    #                     'status' : True,
    #                     'detail' : 'OTP sent successfully.'
    #                     })

    #         else:
    #             return Response({
    #                 'status' : False,
    #                 'detail' : 'Sending OTP error.'
    #                 })

    # else:
    #     return Response({
    #         'status' : False,
    #         'detail' : 'Phone number is not given in post request.'
    #         })


# def send_otp(phone):
#     if phone:
#         key = random.randint(153688,989638)
#         print(key)
#         return key
#     else:
#         return False

class ValidateOTP(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        otp_sent = request.data.get('otp', False)

        if phone and otp_sent:
            old = Phone.objects.filter(phone__iexact=phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    return Response({
                        'status': True,
                        'detail': 'OTP mactched. Please proceed for registration.'
                    })

                else:
                    return Response({
                        'status': False,
                        'detail': 'OTP incorrect.'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'First proceed via sending otp request.'
                })
        else:
            return Response({
                'status': False,
                'detail': 'Please provide both phone and otp for validations'
            })


@api_view(['GET', 'POST'])
def task(request):
    tas = Task.objects.all()
    serializer = TaskSerializer(tas, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'POST'])
def task_read(request, pk):
    tas = Task.objects.get(id=pk)
    serializer = TaskSerializer(tas, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def task_create(request):
    # (request.data )  Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    tas = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tas, data=request.data)

   
    if serializer.is_valid():
        # save() it will save the record
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_del(request, pk):
    tas = Task.objects.get(id=pk)
    tas.delete()
    return Response('data deleted')


# This view will use the default renderers, parsers, authentication classes etc specified in the settings.

@api_view(['GET'])
def hello(request):
    return response({'messsage': 'notreached'})

# By default only GET methods will be accepted. Other methods will respond with "405 Method Not Allowed". To alter this behaviour, specify which methods the view allows, like so:


@api_view(['GET', 'POST'])
def para(request):
    if request.method == 'POST':
        return Response({'mesage': 'reached', 'data': request.data})
    return Response( status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'unable to reach'})


# class based views

class listitem(APIView):

    permission_classes = [IsAuthenticated]
    # permission_classes= [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # if logged in can see and create data ,  if notlogged in he can only see data but cant create data
    #renderer_classes = [JSONRenderer]

    def get(self, request):
        items = item.objects.all()

        serilaizer = ItemSerializer(items, many=True)
        return Response(serilaizer.data)

    def put(self, request, pk, format=None):
        items = item.objects.get(id=pk)
        serializer = ItemSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_obj(self, request, pk, format=None):
    #     items = item.objects.get(id=pk)
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)


class exampleview(APIView):

    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response({'data': request.data})

# REST framework includes a number of built in Parser classes, that allow you to accept requests with various media types

# class FileUploadView(views.APIView):
#     parser_classes = [FileUploadParser]
#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         return Response(status=204)


# generic views


class studList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = stud.objects.all()

    serializer_class = StudSerializer
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     user = self.request.user
    #     return user.accounts.all()

    def get(self, request, *args, **kwargs):
        #     # return super().get_queryset(*args, **kwargs).filter(
        #     #     user=self.request.user
        #     # )

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class studDetail(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = stud.objects.all()
    serializer_class = StudSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        finally:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)
        finally:
            return Response(status=status.HTTP_502_BAD_GATEWAY)


# Using generic class-based views------------------------------------------------------------

class STUD(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializer
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return stud.objects.filter(skill=user)


class STUDD(generics.RetrieveUpdateDestroyAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializer


# using hyperlinkmodelserilazer

# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create()

class Man(viewsets.ModelViewSet):

    queryset = man.objects.all()
    serializer_class = ManSerializer
    # if logged in then only we can see data
    permission_classes = [IsAuthenticated]
#     # authentication_classes = [SessionAuthentication]
#     # authentication_classes = [authentication.TokenAuthentication]

   # using filter, search, ordering options


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class Woman(viewsets.ModelViewSet):
    queryset = woman.objects.all()

    serializer_class = womanSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [authentication.TokenAuthentication]
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    name = 'woman-list'
    filter_fields = ('cook', 'symbol',)
    search_fields = (
        '^cook', '^symbol',
    )
    ordering_fields = (
        'price', 'cook',
    )


# filtering method


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # renderer_classes = [JSONRenderer]
    # renderer_classes = [BrowsableAPIRenderer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'id']


# class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
#     def get_default_renderer(self, view):
#         return JSONRenderer()


# you might need to restrict users to only being able to see objects they created.

# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)


# throttle decorators

# from rest_framework.decorators import api_view, throttle_classes
# from rest_framework.throttling import UserRateThrottle

# # to create a view that uses a throttle to ensure it can only be called once per day by a particular user, use the @throttle_classes decorator, passing a list of throttle classes:

# class OncePerDayUserThrottle(UserRateThrottle):
#     rate = '1/day'

# @api_view(['GET'])
# @throttle_classes([OncePerDayUserThrottle])
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})


# To override the default schema generation for function based views you may use the @schema decorator


# html forms ,

# from .models import profile
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView


# class ProfileList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_list.html'

#     def get(self, request):
#         queryset = profile.objects.all()  # showing data
#         return Response({'profiles': queryset}) # result


# from django.shortcuts import get_object_or_404

# class ProfileDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_detail.html'

#     def get(self, request, pk):
#         profilee = get_object_or_404( profile, pk=pk)
#         serializer = ProfileSerializer(profilee)
#         return Response({'serializer': serializer, 'profile': profilee})
#     def post(self, request, pk):
#         profilee = get_object_or_404(profile, pk=pk)
#         serializer = ProfileSerializer(profilee, data=request.data)  # request.data = to access JSON data for 'POST', 'PUT' and 'PATCH' requests.
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profilee})
#         serializer.save()
#         return redirect('/profile')
# # login form

# class login(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     serializer_class = LoginSerializer
#     template_name = 'login.html'


#     def get(self,request):
#         return Response('Success', status=status.HTTP_200_OK)

#     def post(self, request):
#         user = request.data.get('user',{})

#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# from rest_framework.parsers import FormParser, MultiPartParser,FileUploadParser,BaseParser

# class login(APIView):
#     # renderer_classes = [TemplateHTMLRenderer]
#     serializer_class = UserSerializer
#     parser_classes= [FormParser]
#     template_name = 'login.html'
#     def get(self, request):
#         profilee = get_object_or_404( User)
#         serializer = UserSerializer(profilee)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer= UserSerializer(User,data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# class uploadd(APIView):
#     parser_classes= [FormParser, MultiPartParser,FileUploadParser]
#     def post(self,request, format=None):
#         serializer = UploadSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response()
#     def get(self, request):
#         profilee = get_object_or_404( upload)
#         serializer = UploadSerializer(profilee)
#         return Response({'serializer': serializer,})


# class FileUploadView(APIView):
#     parser_classes = [FileUploadParser]

#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(status=204)

# class PlainTextParser(APIView):
#     """
#     Plain text parser.
#     """
#     media_type = 'text/plain'

#     def parse(self, stream, media_type=None, parser_context=None):
#         """
#         Simply return a string representing the body of the request.
#         """
#         return stream.read()

@api_view(['GET'])
def all(request):

    alls = srikanth.objects.all()
    ser = SrikanthSerializer(alls, many=True)
    return Response(ser.data)


@api_view(['GET'])
def read(request, pk):
    alls = srikanth.objects.get(id=pk)
    ser = SrikanthSerializer(alls, many=False)
    return Response(ser.data)


@api_view(['POST'])
def create(request):

    serializer = SrikanthSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT','GET'])
def update(request, pk):

    tas = srikanth.objects.get(id=pk)
    serializer = SrikanthSerializer(instance=tas, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    var = srikanth.objects.get(id=pk)
    var.delete()
    return Response('data deleted')
