from urllib.request import urlopen
import time
import json

url = "http://csskp.com/api/v1/machines/details.json"
url2 = "http://csskp.com/api/v1/machines/setting.json"


#----------------details-----------
class details:
    def __init__(self, name):
        self.name = name
    
    def myfunc(self):
        response = urlopen(url)
        data_json = json.loads(response.read())
        b =data_json[self.name]
        return b


#----------------------setting--------------------------
class contsets:
    def __init__(self, name):
        self.name = name
        
    def myfunc(self):
        response2 = urlopen(url2)
        data_json2 = json.loads(response2.read())
        b =data_json2[self.name]
        return b

