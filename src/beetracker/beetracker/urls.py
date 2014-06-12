from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import overview, detail, home, dataviz, heatmap_geojson
from core.api import ActivityIndicationResource
from tastypie.api import Api
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns



v1_api = Api(api_name='v1')
v1_api.register(ActivityIndicationResource())


urlpatterns = patterns('',
 (r'^i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += i18n_patterns('',
    # Examples:
    url(r'^overview/', overview),
    url(r'^heatmap/json/', heatmap_geojson),    
    url(r'^dataviz/', dataviz),    
        
	url(r'^detail/(?P<aid>\d+)', detail),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', home, name='home'),
    
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )