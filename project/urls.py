from django.conf.urls import *
from django.contrib import admin
from libscampi.contrib import cms 

admin.autodiscover()

urlpatterns = patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
	url(r'^tv-schedule-forward/(?P<key>\w+)/$', 'project.redirectors.tv_channel_schedule', name="channel-today"),
    url(r'^tv-episode-forward/(?P<id>\w+)/$', 'project.redirectors.tv_episode_detail', name="episode-detail"),
    (r'', include(cms.site.urls))  
)
