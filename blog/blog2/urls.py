from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog2.views import home_view

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
)
