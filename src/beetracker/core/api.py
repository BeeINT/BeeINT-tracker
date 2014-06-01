from tastypie.resources import ModelResource
from core.models import ActivityIndication
from tastypie.authorization import Authorization


class ActivityIndicationResource(ModelResource):
    class Meta:
        queryset = ActivityIndication.objects.all()
        authorization= Authorization()