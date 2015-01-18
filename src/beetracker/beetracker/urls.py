from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from core.views import overview, detail, home
#from core import views #import core
#from beetracker import core
#import beetracker
#from core.api import ActivityIndicationResource
#from tastypie.api import Api
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

#print(beetracker)
import core

#print(core.utils)
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
    #url(r'^apiaries/list/', core.views.apiaries_list, name="apiaries_list"),
    #url(r'^apiaries/detail/(?P<aid>\d+)', core.views.apiaires_detail, name="apiaries_detail"),
    #url(r'^apiaries/new/', core.views.apiaires_new, name="apiaries_new"),
    
    #not implemented
    #url(r'^heatmap/json/', heatmap_geojson),
    #url(r'^dataviz/', dataviz),

    #url(r'^about/', core.views.about, name="about"),

    #url(r'^accounts/register/', core.views.register, name="register"),
    #url(r'^accounts/login/', core.views.user_login, name="login"),
    #url(r'^accounts/logout/', core.views.user_logout, name="logout"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', core.views.home, name='home'),
)
