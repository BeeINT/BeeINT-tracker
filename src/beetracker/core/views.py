
# Create your views here.

from core.models import Apiary

from core.osm import get_thing_by_tag, get_count_from_tag

from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})



def overview(request):
    return render(request, "overview.html", {'apiaries': Apiary.objects.all()})


def detail(request, aid):
    apiary = Apiary.objects.get(id=aid)

    natural_tree_species = get_thing_by_tag(apiary = apiary, tag_key="natural", tag_value="tree", thing=["species:de", "species", "name:botanical"])
    natural_tree_type = get_thing_by_tag(apiary = apiary, tag_key="natural", tag_value="tree", thing=["type"])
    number_trees = get_count_from_tag(apiary = apiary, tag_key="natural", tag_value="tree")
    leisure_parks = get_thing_by_tag(apiary=apiary, tag_key="leisure", tag_value="park")
    landuse_vineyards = get_thing_by_tag(apiary=apiary, tag_key="landuse", tag_value="vineyard")
   

    return render(request, "detail.html", {
        'apiary': apiary,
        'apiaries': Apiary.objects.all(),
        'number_trees': number_trees,
        'natural_tree_species': natural_tree_species, 
        'natural_tree_type': natural_tree_type,
        'leisure_park_chart': leisure_parks, 
        'landuse_vineyard_chart':landuse_vineyards,
        })