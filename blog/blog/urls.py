from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index, add_blog, add_tag, tag_search

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^add_blog/', add_blog, name='add_blog'),
    url(r'^add_tag/', add_tag, name='add_tag'),
    url(r'^tags/(?P<slug>[^\.]+)/$', tag_search, name='tag_search'),
)
