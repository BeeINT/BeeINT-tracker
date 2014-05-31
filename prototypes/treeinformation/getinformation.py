#!/usr/bin/env python
# -*- coding: utf-8 -*-

#using http://overpass-turbo.eu/?key=natural&value=tree&template=key-value


import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

center = {'lat' : 50.055154944, 
  'lon' : 8.21416854858}

lat_delta=0.0502868487461
lon_delta=0.0675487518311

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
  locale.format("%.20f", center['lat']-lat_delta),
  locale.format("%.20f", center['lon']-lon_delta),
  locale.format("%.20f", center['lat']+lat_delta),
  locale.format("%.20f", center['lon']+lon_delta)
  )


import simplejson as json
#import urllib
#import urllib2

#data = urllib.urlencode( {'data': DATA_QUERY})
#req = urllib2.Request(API_URL, data)
#response = urllib2.urlopen(req)
#the_page = response.read()
#print the_page

response = json.load(file("test.json"))
trees = response["elements"]

print "Trees: {0}".format(len(trees))


species = {}
leafs = {}

for tree in trees:
  if "species" in tree["tags"]:
    if tree["tags"]["species"] in species:
      species[tree["tags"]["species"]] += 1
    else:
      species[tree["tags"]["species"]] = 1
  elif "name:botanical" in tree["tags"]:
    if tree["tags"]["name:botanical"] in species:
      species[tree["tags"]["name:botanical"]] += 1
    else:
      species[tree["tags"]["name:botanical"]] = 1

  if "type" in tree["tags"]:
    if tree["tags"]["type"] in leafs:
      leafs[tree["tags"]["type"]] += 1
    else:
      leafs[tree["tags"]["type"]] = 1


print "writing to file vegetation.json"

data = [
  {
    "name" : "Species",
    "id" : "tree_species",
    "data": species, 
  },
  {
    "name" : "Leafs",
    "id" : "tree_leafs",
    "data": leafs, 
  },
]

f = file("vegetation.json", "w")
st = json.dumps(data)
f.write(st)

#
#{
#  "type": "node",
#  "id": 343464147,
#  "lat": 50.0869212,
#  "lon": 8.2609405,
#  "tags": {
#    "name": "großer Mammut-Baum",
#    "name:botanical": "Sequoiadendron Giganteum",
#    "natural": "tree"
#  }