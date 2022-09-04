
from django.urls import path

from .import views
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

# 
urlpatterns = [

    path('employ/', views.allEmployees, name='all_employees'),

    path('employ/<str:pk>', views.oneEmploye, name='one_employees'),

    path('del/<str:pk>', views.employDeletion, name='emp_del'),

    path('create/', views.employCreate, name='employ_create'),

    path('update/<str:pk>', views.employUpdate, name='emp_update'),

    #path('u/<str:pk>', views.update.as_view()),

    #path('task_read/<str:pk>', views.task_read, name='task_read'),
   
   

]