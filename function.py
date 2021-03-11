from database import Database
from connection import activate
import datetime
import requests

#Global variables
key=activate()
dtoday= datetime.date.today()
link = (f'https://api.resrobot.se/v2/trip?key={key}')
origin = []
destination=[]
stops=[]
idx=[]
product=[]
db = Database()

"""
The search_now function retrieves data for immediately available journeys. It takes two variables. An orgin &
destination name e.g stockholm cetral station to uppsala 
"""

def search_now(sfrom, to):
    global link
    global dtoday
    numF =6
    db.cursor.execute(f'SELECT stop_id FROM stops Where stop_name = %s', sfrom)
    row0 =db.cursor.fetchone()
    row= ''.join(row0)
    db.cursor.execute(f'SELECT stop_id FROM stops Where stop_name = %s' , to)
    row1= db.cursor.fetchone()
    row2=''.join(row1)
    now = datetime.datetime.now()
    time_now= now.strftime("%H:%M:%S")
    url = f'{link}&originId={row}&destId={row2}&format=json&date={dtoday}&time={time_now}&numF={numF}$DisableLegtype"WALK"== 0'
    response = requests.get(url)
    data = response.json()["Trip"]

    leg= []
    for x in range(len(data)):
        for k in data[x]["LegList"]:
            if  k == "Leg":
                leg.append(data[x]["LegList"][k])
    for d in leg:
        print(d["Destination"])





    #process_data_to_dictionary(data)
    #process_data_to_dictionary(data)


def process_data_to_dictionary(data):
    global origin
    global departure
    global stops
    test={}
    for k, v in data.items():
        for k1 in v:
            for key in k1:
                if key == "LegList":
                    leg_list = k1[key]
                    for key1 in leg_list:
                        if key1 == "Leg":
                            leg = leg_list[key1]
                            for x in range(len(leg_list)):
                                for p in leg[x]:
                                    if p == "Origin" or p=="Destination" or p== "Product" or p== "stops":
                                        test ={"Origin: ": (leg[x][p])}


    for x in origin:
        print(x["name"])



"""   origin.append(leg[0]["Origin"]["name"])
    origin.append(leg[0]["Origin"]["time"])
    origin.append(leg[0]["Origin"]["date"])
    destination.append(leg[0]["Destination"]["name"])
    destination.append(leg[0]["Destination"]["time"])
    destination.append(leg[0]["Destination"]["date"])
    stops.append(leg[0]["stops"]["name"])
    stops.append(leg[0]["stops"]["arrTime"])
    stops.append(leg[0]["stops"]["depTime"])
    if leg[0]["stops"]["arrDate"]:
        stops.append(leg[0]["stops"]["arrDate"])
    idx.append(leg[0]["idx"]["name"])
    idx.append(leg[0]["idx"]["type"])
    product.append(leg[0]["Product"]["name"])
    product.append(leg[0]["Product"]["operatorUrl"])


 def proceess_recurse(data):    
    for key in data:
       v =data[key]
       if isinstance(v, dict):
            r.extend(iterate_dict(v, parents + [k]))
       elif isinstance(v, list):
            r.append((k, v, parents))
        else:
            r.append((k, v, parents))"""

