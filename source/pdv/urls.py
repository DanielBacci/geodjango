"""pdv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from rest_framework.documentation import include_docs_urls


def ping(request):
    return HttpResponse('pong')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r'^docs/',
        include_docs_urls(
            title='Parceiro Magalu API',
            authentication_classes=tuple(),
            permission_classes=tuple()
        )
    ),
    url(
        r'^oauth/',
        include(
            (
                'oauth2_provider.urls'
            ),
            namespace='oauth2_provider'
        )
    ),
    path(
        '',
        include('pdv.partners.urls'),
    ),
    path('ping/', ping),
]
