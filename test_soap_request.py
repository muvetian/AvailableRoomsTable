import xml.etree.ElementTree as ET
import requests

url="http://ems.davidson.edu/emsapi/service.asmx?op=GetBuildings"

headers = {'content-type': 'text/xml','charset':'utf-8'}
body = """<?xml version="1.0" encoding="UTF-8"?>
         <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
         <soap:Body>
         <GetBuildings xmlns="http://DEA.EMS.API.Web.Service/">
         <UserName>emsapi</UserName>
         <Password>emsapi</Password>
         </GetBuildings>
         </soap:Body>
         </soap:Envelope>"""

response = requests.post(url,data=body,headers=headers)
root = ET.fromstring(response.content)
# print len(root.findall('Description'))
print root.find('.//{http://DEA.EMS.API.Web.Service/}GetBuildingsResult')
# print response.content