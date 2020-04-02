from IPython.core.magic import register_line_magic
import sys, os
import requests,json

@register_line_magic
def weather(line):
    city_name = line
    api_key = "435348aa7ec3b2ac924fd375be949b2a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    if requests is not None:
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        return requests.get(complete_url).json() 
    return "error"

def load_ipython_extension(ipython):
    ipython.register_magic_function(weather, 'line') 
    try:
        import requests,json
        ipython.push({"weather": weather, "requests": requests, "json": json})  # Add to users namespace
    except ImportError:
        pass
