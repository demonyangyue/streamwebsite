from django.conf.urls.defaults import *
from mystreaming.apps.xml_RPC.views import showSource, playSource
urlpatterns = patterns('',
        (r'show_source$', showSource, {'template_name':'xml_RPC/show_source.html'}),
        (r'play_source/(?P<source_name>.+)$', playSource, {'template_name':'xml_RPC/play_source.html'}),
)
