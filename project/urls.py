from django.conf.urls import url, include
from django.contrib import admin
from libscampi.contrib.cms.sites import site
from project import redirectors

admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tv-schedule-forward/(?P<key>\w+)/$', redirectors.tv_channel_schedule, name="channel-today"),
    url(r'^tv-episode-forward/(?P<id>\w+)/$', redirectors.tv_episode_detail, name="episode-detail"),
    url(r'', include(site.urls))
]
