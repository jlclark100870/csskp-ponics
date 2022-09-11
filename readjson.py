from urllib.request import urlopen
import time
import json
from datetime import *

url = "http://csskp.com/api/v1/machines/details.json"
url2 = "http://csskp.com/api/v1/machines/week1.json"


#----------------details-----------
class details:
   
    def __init__(self, name):
        self.name = name
        
    def myfunc(self):
    
        response2 = open('details.json')
        data_json2 = json.load(response2)
        b =data_json2[self.name]
       
        return b

#----------------------setting--------------------------
class contsets:
    
    def __init__(self, name):
        self.season = self.grow_time()
        self.name = name
        self.myfunc()

    def grow_time(self):
        response = urlopen(url2)
        data_json = json.loads(response.read())
        b =data_json["plantdate"]
        k = datetime.strptime(b, "%m/%d/%Y")
        j = date.today
        grow_period = datetime.date(k) - date.today()
        grow_days = grow_period.total_seconds()
        tgrow_period = (grow_days /60)/60/24

        if abs(tgrow_period) < int(data_json["daysseeding"]) :
            season = "seeding"
        elif abs(tgrow_period) >=data_json["daysseeding"] and abs(tgrow_period) < data_json["daysmature"] :
            season = "bloom"
        elif abs(tgrow_period) >= data_json["daysmature"]:
            season = "mature"
        
        return(season)

    
    def myfunc(self):
    
        response = urlopen(url2)
        data_json = json.loads(response.read())
        qvalue =data_json[self.season][self.name]
        b = qvalue
        return b

    
      
class globalset:
    def __init__(self, name):
        self.name = name
        self.myfunc()

    def myfunc(self):
    
        response = urlopen(url2)
        data_json = json.loads(response.read())
        qvalue =data_json[self.name]
        if self.name == 'plantdate' :
             b =data_json["plantdate"]
             k = datetime.strptime(b, "%m/%d/%Y")
             j = date.today
             grow_period = datetime.date(k) - date.today()
             grow_days = grow_period.total_seconds()
             qvalue = (grow_days /60)/60/24

        b = abs(qvalue)
        return b

# p1 = contsets('PH')
# myfunc_results = p1.myfunc()
# print(myfunc_results)