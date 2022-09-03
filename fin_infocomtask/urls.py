
from django.urls import path

from .import views
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

# 
urlpatterns = [

    path('employ/', views.all_employees, name='all_employees'),

    path('employ/<str:pk>', views.one_employe, name='one_employees'),

    path('del/<str:pk>', views.emp_del, name='emp_del'),

    path('create/', views.employ_create, name='employ_create'),

    path('update/<str:pk>', views.emp_update, name='emp_update'),

    #path('u/<str:pk>', views.update.as_view()),

    #path('task_read/<str:pk>', views.task_read, name='task_read'),
   
   

]