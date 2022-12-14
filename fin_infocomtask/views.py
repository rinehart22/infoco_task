
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view


# The @api_view decorator for working with function based views.
@api_view(['GET'])
def allEmployees(request):

    try:
        # getting queryset from the database
        employee_data = Employee.objects.all()
    # many=true : it tell drf that querset contain multiple items
        serializer = EmployeeSerializer(employee_data,  many=True)
        print(serializer)
    # here serializer will convert that queryset into python_ditionary and into json format
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'no data found',
                         'success': 'false'},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def employDeletion(request, pk):
    try:
        # retrieve one record from the database using id
        deletion_of_employe = Employee.objects.get(id=pk)
        deletion_of_employe.delete()
        return Response({'message': 'employee deleted successfully',
                         'success': 'true'},
                        status=status.HTTP_200_OK)
    except:
        return Response({'message': 'no employee found with this regid',
                         'success': 'false'},
                        status=status.HTTP_200_OK)


@api_view(['GET'])
def oneEmploye(request, pk):
    # to prevent program to stop execution and handles exceptions
    try:
        # retrieve one record from the database using id if data was found
        getOneEmploy = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(getOneEmploy, many=False)
        return Response(serializer.data,
                        {'message': 'employee details found',
                         'success': 'true'},
                        status=status.HTTP_200_OK,)
    except:
        # it will execute when no data found and throws a message to the user
        return Response({'message': 'employee details not found',
                         'success': 'false'},
                        status=status.HTTP_200_OK,)


@api_view(['POST', 'GET'])
# POST this method will send data to the database
def employCreate(request):
    if request.method == 'POST':

        try:
            # (request.data )  Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
            data = request.data
            if Employee.objects.filter(email=data.get('email')).exists():
                # The exists() method is used to check the result of the query. Returns True if the queryset contains any results, and False if not.

                return Response({'message': 'employe already exist',
                                'success': 'false'}, status=status.HTTP_200_OK)

            return Response({'message': 'employee created failed',
                             'success': 'false'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            serializer = EmployeeSerializer(data=request.data)
            # is_valid :Deserializes and validates incoming data,
            # method takes an optional raise_exception flag that will cause it to raise a serializers.               ValidationError exception if there are validation errors
            if serializer.is_valid():
                # save() it will save the record for the user
                serializer.save()
                print(serializer)
                content = {
                    'message': 'employee created successfully',
                    'regid': "with '{}'".format(id),
                    'success': 'true'}
                
                return Response(content)

            return Response({'message': 'invalid body request',
                             'success': 'false'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response({'message': 'fill the details',
                         'success': 'true'}, status=status.HTTP_200_OK)


# updating the record-------------------------------------------------------------------------------------

@api_view(['PUT', 'GET'])
# PuT this method creates a new resource or updates (substitutes) a representation of the target resource with the request payload
def employUpdate(request, pk):
    if request.method == 'PUT':
        try:
            updateData = Employee.objects.get(id=pk)
        except Exception:
            return Response({'message': 'employee not exist', 'success': 'false'}, status=status.HTTP_200_OK)
            # instance: it is an object which we get from database before updating

        try:
            serializer = EmployeeSerializer(
                instance=updateData, data=request.data, many=False)
            print(serializer,'iiiiiiiiiiiiiiiiiiiiiii')
            if serializer.is_valid():
                serializer.save()
                print(serializer.data,'yyyyyyyyyyyyyyyyyyyyyyyyy')
                return Response({'message': 'employee details updated successfully', 'success': 'true'}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'invalid body request',
                                 'success': 'false'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'employee updation failed',
                             'success': 'false'}, status=status.HTTP_200_OK)

    else:
        # to prevent program to stop execution and handles exceptions
        try:
            # retrieve one record from the database using id if data was found
            getOneEmploy = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(getOneEmploy, many=False)
            return Response(serializer.data,
                            )
            # status = status.HTTP_200_OK,)
        except Exception as e:
            # it will execute when no data found and throws a message to the user
            print('---------------------', e)
            return Response({'message': 'employee details not found',
                             'success': 'false'},
                            status=status.HTTP_200_OK,)















# class RegisterAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             print(data)
#             serializer = UserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 # snt_otp()

#                 return Response({

#                     'status': 200,
#                     'message': 'registration successful',
#                     'data': serializer.data,
#                 })

#             return Response({

#                 'status': 400,
#                 'message': 'something went wrong',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
