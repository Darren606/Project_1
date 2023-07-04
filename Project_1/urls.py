"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework.documentation import include_docs_urls
from emp_manage.views.json_views import StaffLoginAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="APIs docs",
        default_version='v1',
        description="Documents",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('django_1.urls')),
    path('api/', include('REST_Framework.urls')),
    path('api/', include('coreAPI.urls')),
    path('admin/', admin.site.urls),
    # path('docs/', include_docs_urls(title='Site API'))]

    re_path(r'^api/', include("emp_manage.urls")),
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
