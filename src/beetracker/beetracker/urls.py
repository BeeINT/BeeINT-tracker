from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import overview, detail, home
from core.api import ActivityIndicationResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(ActivityIndicationResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^overview/', overview),
	url(r'^detail/(?P<aid>\d+)', detail),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
