from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import authenticate, login

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'gdt_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       url('^', include('django.contrib.auth.urls')),
)
