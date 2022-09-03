from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from sysconfig import get_scheme_names
from django.urls import path, re_path

from .import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router1.register('data', views.Woman, basename='woman')

router = routers.SimpleRouter()
# # define the router path and viewset to be used
router.register(r'man', views.Man)


# schema_view = get_schema_view(
#     title='Example API',
#     renderer_classes=[OpenAPIRenderer],
# )


urlpatterns = [
    #  path('swagger/', schema_view),
    # in case of url use this r' ^ (?P < pk >\d+) /$
    path('', views.BlogPostAPIView.as_view(), name='post-rud'),
    path('blog/<str:pk>', views.BlogPostRudView.as_view(), name='post-rud'),
    path('log/', views.LoginView.as_view()),
    # path('', views.ValidateOTP.as_view()),
    # path('', views.ValidateOTP.as_view()),




    #path('', views.listitem.as_view(), name='list'),
    path('app', views.apioverview, name='apioverview'),
    path('s/', views.all, name='all'),
    path('s/<str:pk>', views.read, name='all'),
    path('sd/<str:pk>', views.delete, name='all'),
    path('ss/', views.create, name='all'),
    path('ss/<str:pk>', views.update, name='all'),



    path('task/', views.task, name='task'),
    path('task_read/<str:pk>', views.task_read, name='task_read'),
    path('task_create/', views.task_create, name='create'),
    path('taskup/<str:pk>', views.task_update, name='up'),
    path('tasdel/<str:pk>', views.task_del, name='del'),
    path('hello', views.hello, name='hel'),
    path('para', views.para, name='para'),



    path('lis/<str:pk>', views.listitem.as_view()),
    path('eg/', views.exampleview.as_view()),

    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),

    path('stud/', views.studList.as_view()),
    path('stud/<str:pk>', views.studDetail.as_view()),

    path('STUD/', views.STUD.as_view()),
    path('STUD/<str:pk>', views.STUDD.as_view()),


    path('users/', views.UserList.as_view(), name='user-list'),





    # path('apps', views.view, name= 'apioverview' ),


    path('swagger-ui/', TemplateView.as_view(

         template_name='swagger-ui.html',
         extra_context={'schema_url': 'openapi-schema'}

         ), name='swagger-ui'),


    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),


    # hyperlinkmodel urls
    path('mans/', views.Man.as_view({'get': 'list'})),



    # path('profile/', views.ProfileList.as_view()),
    # path('profiled/<str:pk>', views.ProfileDetail.as_view()),

    # path('login/', views.login.as_view()),

    # path('up/', views.uploadd.as_view()),

    #  path('plain/', views.PlainTextParser.as_view()),

    # re_path(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),


    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.


    # path('openapi', get_schema_view(
    #     title="frame",
    #     description="API for all things …",
    #     version="1.0.0",  url='',
    # ), name='openapi-schema'),

]


urlpatterns += router.urls + router1.urls + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += router1.urls


# or

# urlpattern = [ path('', include(router.urls) ]

# urlpatterns = format_suffix_patterns(urlpatterns)
