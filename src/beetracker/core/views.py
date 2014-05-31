#from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
# Create your views here.

from core.models import Apiary, MapInformation

import simplejson as json


def home(request):

    template = loader.get_template('home.html')
    context = Context()
    return HttpResponse(template.render(context))



def overview(request):

    template = loader.get_template('overview.html')
    context = Context({'apiaries': Apiary.objects.all()})
    return HttpResponse(template.render(context))


def detail(request, aid):

    apiary = Apiary.objects.get(id=aid)
    mapinfos = MapInformation.objects.filter(apiary = apiary)


    for mapinfo in mapinfos:

        response = json.loads(mapinfo.api_response)
        findings = response["elements"]

        if mapinfo.tag_key == "natural" and mapinfo.tag_value == "tree":
            species = {}
            leafs = {}

            for tree in findings:
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
            mapinfo.charts = [
                {
                    "name" : "Species",
                    "id" : "pecies",
                    "data": species
                },
                {
                    "name" : "Leafs",
                    "id" : "leafs",
                    "data": leafs
                },
                ]




    template = loader.get_template('detail.html')
    context = Context({
        'apiary': apiary,
        'mapinfos': mapinfos
        })
    return HttpResponse(template.render(context))