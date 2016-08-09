"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [

    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^pattern/$', views.pattern, name='patterns'),
    url(r'^patterns/(?P<slug>[-\w]+)/$', views.pattern_detail, name="pattern_detail"),
    url(r'^illustration/$', views.illustration, name='illustrations'),
    url(r'^illustrations/(?P<slug>[-\w]+)/$', views.illustration_detail, name='illustration_detail'),
    url(r'^sketchbook/$', views.sketchbook, name='sketchbooks'),
    url(r'^sketchbooks/(?P<slug>[-\w]+)/$', views.sketchbook_detail, name="sketchbook_detail"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, })
    ]
