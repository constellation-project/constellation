"""constellation URL Configuration

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
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

# If Django Rest Framework is installed, then add a REST API
try:
    from rest_framework import routers
except ImportError:
    pass
else:
    from layers.api import views

    router = routers.DefaultRouter()
    router.register(r'subnet', views.SubnetViewSet)
    router.register(r'vlan', views.VlanViewSet)

    urlpatterns += [
        url(r'^api/', include(router.urls)),
    ]
