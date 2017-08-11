from django.conf.urls import  url

from django.contrib import admin
#admin.autodiscover()

#from django.conf import settings
#from django.conf.urls.i18n import i18n_patterns


#urlpatterns = [
#    (r'^i18n/', include('django.conf.urls.i18n')),
#)

#if 'rosetta' in settings.INSTALLED_APPS:
#    urlpatterns += i18n_patterns('',
#        url(r'^admin/rosetta/', include('rosetta.urls')),
#    )

import core.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/en/', permanent=False), name='index'),
    url(r'^heatmap/json/', core.views.heatmap_geojson),
    
]


urlpatterns += i18n_patterns(
    #login required
    url(r'^apiaries/list/', core.views.apiaries_list, name="apiaries_list"),
    url(r'^apiaries/detail/(?P<aid>\d+)', core.views.apiaries_detail, name="apiaries_detail"),
    
    url(r'^dataviz/', core.views.dataviz, name="dataviz"),
    url(r'^admin/', admin.site.urls),

    url(r'^$', core.views.home, name='home')
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

