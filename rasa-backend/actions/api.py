import requests
import xmltodict, json

def prlist():
    api_address='http://172.26.0.121:8002/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV/A_PurchaseRequisitionHeader'
    # city = input('Enter the City Name :')
    url = api_address
    xml_data = requests.get(url)
    obj = xmltodict.parse(xml_data)
    js = json.dumps(obj)
    js_obj = json.loads(js)
    values = js_obj['feed']['entry']
    prnumber=[]
    for i in values:
        prnumber.append(i['content']['m:properties']['d:PurchaseRequisition'])
    return prnumber

# def prdetails(prno):
#     api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#     # city = input('Enter the City Name :')
#     url = api_address + prno
#     json_data = requests.get(url).json()
#     format_add = json_data['main']
#     print(format_add)
#     # print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
#     #     json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
#     return format_add

# def prupdate(prno):
#     api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#     # city = input('Enter the City Name :')
#     url = api_address + prno
#     json_data = requests.get(url).json()
#     format_add = json_data['main']
#     print(format_add)
#     # print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
#     #     json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
#     return format_add

# def prdelete(prno):
#     api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#     # city = input('Enter the City Name :')
#     url = api_address + prno
#     json_data = requests.get(url).json()
#     format_add = json_data['main']
#     print(format_add)
#     # print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
#     #     json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
#     return format_add