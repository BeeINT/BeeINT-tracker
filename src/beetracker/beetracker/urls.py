from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import overview, detail, home
import core
#from core.api import ActivityIndicationResource
#from tastypie.api import Api
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


#v1_api = Api(api_name='v1')
#v1_api.register(ActivityIndicationResource())

urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns('',
        url(r'^admin/rosetta/', include('rosetta.urls')),
    )

urlpatterns += i18n_patterns('',
    #login required
    url(r'^overview/', overview, name="overview"),
    url(r'^detail/(?P<aid>\d+)', detail),

    #not implemented
    #url(r'^heatmap/json/', heatmap_geojson),
    #url(r'^dataviz/', dataviz),

    url(r'^accounts/register/', core.views.register, name="register"),
    url(r'^accounts/login/', core.views.user_login, name="login"),
    url(r'^accounts/logout/', core.views.user_logout, name="logout"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
)
