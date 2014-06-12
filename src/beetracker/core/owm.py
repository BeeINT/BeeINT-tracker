from core.models import MapInformation
import simplejson as json



def get_current_weather_temp(apiary):
    try:
        map_obj = MapInformation.objects.filter(apiary = apiary, tag_key="weather", tag_value="now").latest()
        ret = json.loads(map_obj.api_response)["main"]["temp"] -273.15 #convert from kelvin to celcius
    except Exception:
        ret = None
    return ret


def get_current_weather_humidity(apiary): 
    try:
        map_obj = MapInformation.objects.filter(apiary = apiary, tag_key="weather", tag_value="now").latest()
        ret = json.loads(map_obj.api_response)["main"]["humidity"] 
    except Exception:
        ret = None
    return ret
