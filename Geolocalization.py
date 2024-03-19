import json
import requests

def geolocalizate_ip(ip):
    api_url = "http://ip-api.com/json/"
    parametros = ["country","lat","lon","timezone"]
    data = {"fields":parametros}
    
    res = requests.get(api_url+ip, data=data)
    api_json_res = json.loads(res.content)
        
    country=api_json_res[parametros[0]]
    coords=(int(api_json_res[parametros[1]]),int(api_json_res[parametros[2]]))
    time_zone=api_json_res[parametros[3]]
    
    return country, coords, time_zone

ip="158.156.23.5"
print(geolocalizate_ip(ip))
