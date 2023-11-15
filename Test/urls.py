"""
URL configuration for Test project.

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
from django.urls import path
from Test import views
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DevJunction API",
        default_version="v1",
        description="DevJunction  API",
        terms_of_service="<https://www.google.com/policies/terms/>",
        contact=openapi.Contact(email="contact@devjunction.in"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

urlpatterns = [
    # For the OpenAPI documentation
    re_path(
        r"^swagger(?P<format>\\.json|\\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path('docs/yaml', schema_view.without_ui(cache_timeout=0),),
    re_path(
        r"^api/docs/swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/docs/redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    #Our paths
    path('admin/', admin.site.urls),
    path('api/city', views.city),
    path('api/member', views.member),
    path('api/trainer', views.trainer),
    path('api/sport', views.sport),
    path('api/coursedate', views.coursedate),
    path('api/course', views.course),
    path('api/participant', views.participant),
    path('api/register', views.register),
    path('api/toggle-staff', views.toggle_staff_status),
    path('api/login', views.user_login),
    path('api/check-auth', views.check_valid_token),
    path('api/logout', views.logout),
]
