#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf8')
#import simplejson as json
import urllib
import urllib2
from datetime import datetime    
from decimal import Decimal

# Register your models here.

from core.models import Apiary, MapInformation, Hive, HAPlacement, ActivityIndication

def get_mapinfos(modeladmin, request, queryset):
    lat_delta=Decimal(0.0502868487461)
    lon_delta=Decimal(0.0675487518311)

    for apiary in queryset:


        API_URL = "http://overpass-api.de/api/interpreter"
        DATA_QUERY = """<?xml version="1.0" encoding="UTF-8"?>
        <osm-script output="json" timeout="25">
          <!-- gather results -->
          <union>
            <!-- query part for: “natural=tree” -->
            <query type="node">
              <has-kv k="natural" v="tree"/>
              <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
            </query>
            <query type="way">
              <has-kv k="natural" v="tree"/>
              <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
            </query>
            <query type="relation">
              <has-kv k="natural" v="tree"/>
              <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
            </query>
          </union>
          <!-- print results -->
          <print mode="body"/>
          <recurse type="down"/>
          <print mode="skeleton" order="quadtile"/>
        </osm-script>""".format(
          locale.format("%.20f", apiary.latitude-lat_delta),
          locale.format("%.20f", apiary.longitude-lon_delta),
          locale.format("%.20f", apiary.latitude+lat_delta),
          locale.format("%.20f", apiary.longitude+lon_delta)
          )


        data = urllib.urlencode( {'data': DATA_QUERY})
        req = urllib2.Request(API_URL, data)
        response = urllib2.urlopen(req).read()
        mapinfo = MapInformation()
        mapinfo.api_response = response
        mapinfo.tag_key = 'natural'
        mapinfo.tag_value = 'tree'
        mapinfo.apiary = apiary
        mapinfo.date = datetime.now()
        mapinfo.save()



class ApiaryAdmin(admin.ModelAdmin):
    actions = [get_mapinfos]


admin.site.register(Apiary, ApiaryAdmin)
admin.site.register(MapInformation)
admin.site.register(Hive)
admin.site.register(HAPlacement)

admin.site.register(ActivityIndication)
