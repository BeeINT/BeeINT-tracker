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

from math import pi, cos
# Register your models here.

from core.models import Apiary, MapInformation, Hive, HAPlacement, ActivityIndication


def move_geo(latitude, longitude, dx, dy):
    dx = Decimal(dx)
    dy = Decimal(dy * 2) #TODO: WHY? WHY DO I NEED THIS? 
    r_earth = Decimal(6378)
    pid = Decimal(pi)
    ohh = Decimal(180)

    box_latitude_top_left  = latitude  + ((dx / r_earth) * (ohh / pid))
    box_longitude_top_left = longitude + ((dy / r_earth) * (ohh / pid)) * Decimal(cos(pid*latitude/ohh))
    return box_latitude_top_left, box_longitude_top_left



def get_mapinfos(modeladmin, request, queryset):


    for apiary in queryset:
        box_latitude_top_left, box_longitude_top_left = move_geo(apiary.latitude, apiary.longitude, -1., -1.)
        box_latitude_bottom_right, box_longitude_bottom_right = move_geo(apiary.latitude, apiary.longitude, 1., 1.)



        for tag_name, tag_key in [["natural", "tree"],["leisure", "park"], ["landuse", "vineyard"]]:
          API_URL = "http://overpass-api.de/api/interpreter"
          DATA_QUERY = """<?xml version="1.0" encoding="UTF-8"?>
          <osm-script output="json" timeout="25">
            <!-- gather results -->
            <union>
              <!-- query part for: “natural=tree” -->
              <query type="node">
                <has-kv k="{4}" v="{5}"/>
                <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
              </query>
              <query type="way">
                <has-kv k="{4}" v="{5}"/>
                <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
              </query>
              <query type="relation">
                <has-kv k="{4}" v="{5}"/>
                <bbox-query s="{0}" w="{1}" n="{2}" e="{3}"/>
              </query>
            </union>
            <!-- print results -->
            <print mode="body"/>
            <recurse type="down"/>
            <print mode="skeleton" order="quadtile"/>
          </osm-script>""".format(
            locale.format("%.20f", box_latitude_top_left),
            locale.format("%.20f", box_longitude_top_left),
            locale.format("%.20f", box_latitude_bottom_right),
            locale.format("%.20f", box_longitude_bottom_right),
            tag_name,
            tag_key
            )


          data = urllib.urlencode( {'data': DATA_QUERY})
          req = urllib2.Request(API_URL, data)
          response = urllib2.urlopen(req).read()
          mapinfo = MapInformation()
          mapinfo.api_response = response
          mapinfo.tag_key = tag_name
          mapinfo.tag_value = tag_key
          mapinfo.apiary = apiary
          mapinfo.date = datetime.now()
          mapinfo.save()




        API_URL = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}".format(apiary.latitude, apiary.longitude)

        req = urllib2.Request(API_URL)
        response = urllib2.urlopen(req).read()
        mapinfo = MapInformation()
        mapinfo.api_response = response
        mapinfo.tag_key = "weather"
        mapinfo.tag_value = "now"
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
