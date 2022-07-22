"""farmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1 import views as a
from app2 import views as b
from app3 import views as c
from app4 import views as d
from app5 import views as e

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^aa1/', a.a1),
    url(r'^aa2/', a.a2),
    url(r'^aa3/', a.a3),
    url(r'^bb1/', b.b1),
    url(r'^bb2/', b.b2),
    url(r'^bb3/', b.b3),
    url(r'^cc1/', c.c1),
    url(r'^cc2/', c.c2),
    url(r'^cc3/', c.c3),
    url(r'^dd1/', d.d1),
    url(r'^dd2/', d.d2),
    url(r'^dd3/', d.d3),
    url(r'^ee1/', e.e1),
    url(r'^ee2/', e.e2),
    url(r'^ee3/', e.e3),
]
