import xml.etree.ElementTree as ET
import requests
import json
import codecs

def get_available_rooms(building):
    building_dict = {'Chambers': 5}
    print (building_dict['Chambers'])  # create another function to create the building_dict by calling soap request get all builidings

    building_id = building_dict[building]
    url="http://ems.davidson.edu/emsapi/service.asmx?op=GetRoomsAvailable"

    headers = {'content-type': 'text/xml','charset':'utf-8'}
    body = """<?xml version="1.0" encoding="UTF-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
        <GetRoomsAvailable xmlns="http://DEA.EMS.API.Web.Service/">
            <UserName>emsapi</UserName>
            <Password>emsapi</Password>
            <BookingDate>2017-04-26</BookingDate>
            <BuildingID>""" + str(building_id) +"""</BuildingID>
            <StartTime>2017-04-26T08:15:00</StartTime>
            <EndTime>2017-04-26T09:15:00</EndTime>
        </GetRoomsAvailable>
        </soap:Body>
        </soap:Envelope>"""

    response = requests.post(url,data=body,headers=headers)
    print(response.content)
    root = ET.fromstring(response.content)
    json_list = root.findall('.//{http://DEA.EMS.API.Web.Service/}GetRoomsAvailableResult')[0].text
    parse = json.loads(json_list)
    return parse['Data']

    


# json_list = root.find('GetRoomsAvailableResult').text
# parse = json.loads(json_list)
# print parse['Data'][1].keys()
# keys = parse['Data'][1].keys()
# def clean_text(text):
#     text = text.replace("\'", " ")
#     text = text.replace("\"", " ")
#     text = text.replace(",", " ")
#     text = text.replace("\r", "")
#     text = text.replace("\n", "")
        
#     return text


# def generate_column():
	
# 	line = ""
# 	for i in range(len(keys)-1):
# 		line += str(keys[i])
# 		line += ","
# 	line += str(keys[len(keys)-1])
# 	line += "\n"
# 	return line


# csvFile = codecs.open("AllBuildings.csv","w","utf-8")
# first_column = generate_column()
# csvFile.write(first_column)
# for dict in parse['Data']:
#     line = ""
#     for i in range(len(dict)):
#         if dict[keys[i]] == None:
#             line += "None"
#         else:
#             line += clean_text(str(dict[keys[i]]));
#         line += ","
#     line +="\n"
#     csvFile.write(line)
# csvFile.close()