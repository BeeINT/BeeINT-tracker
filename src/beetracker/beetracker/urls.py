from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import overview, detail, home

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^overview/', overview),
	url(r'^detail/(?P<aid>\d+)', detail),
    url(r'^admin/', include(admin.site.urls)),
)
