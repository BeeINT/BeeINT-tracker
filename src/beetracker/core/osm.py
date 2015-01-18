from core.utils import soundex
from core.models import MapInformation
import simplejson as json
import traceback, sys

def get_thing_by_tag(apiary, tag_key, tag_value, thing=["name"], soundex = True):
    """
    gets an attribute from a tag. default is ["name"] but i can get the first match of ["value1", "value2"]
    """
    try:
        map_obj = MapInformation.objects.filter(apiary = apiary, tag_key=tag_key, tag_value=tag_value).latest()
        ret = _crunsh_generic(json.loads(map_obj.api_response)["elements"], thing)
        if soundex:
            ret = _magic_combine(ret)
        return sorted(ret.items())
    except Exception as e:
        print(str(e))
        traceback.print_exc(file=sys.stdout)
        return None

    
  
def get_count_from_tag(apiary, tag_key, tag_value):
    try:
        map_obj = MapInformation.objects.filter(apiary = apiary, tag_key=tag_key, tag_value=tag_value).latest()
        return len(json.loads(map_obj.api_response)["elements"])
    except:
        return None



def _crunsh_generic(elements, keys=["name"]):
    data = {}
    for element in elements:
        if "tags" in element:
            for key in keys:
                if key in element["tags"]:
                    if element["tags"][key] in data:
                        data[element["tags"][key]] += 1
                    else:
                         data[element["tags"][key]] = 1
                    break
    return data


def _magic_combine(elements):
    """uses soundex to combine close words. uses the most used word for a soundex group as reference
    """
    # soundex
    ret = {}
    snd_grp = {}
    soundex_keys = {}
    for key in elements:
        snd_key = soundex(key.encode('ascii', 'ignore'))
        if snd_key in ret:
            snd_grp[snd_key] += elements[key]
        else:
            snd_grp[snd_key] = elements[key]
        
        if snd_key in soundex_keys:
            soundex_keys[snd_key].append(key)
        else:
            soundex_keys[snd_key] = [key]
    #remap
    for key in sorted(snd_grp.keys()):
        most = 0
        for key_orig in soundex_keys[key]:
            if elements[key_orig] > most:
                most = elements[key_orig]
                key_best = key_orig
        ret[key_best] = snd_grp[key]
    return ret