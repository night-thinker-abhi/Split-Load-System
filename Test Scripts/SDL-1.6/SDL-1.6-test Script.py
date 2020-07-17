import requests
import socket
import os
import sys
import json
sys.path.append('../../')
from services.getFileDetails import getFileDetails
class MSG:
    master = None
    msg = None
    data = None

    def __init__(self, data, msg="", master=False):
        self.master = master
        self.msg = msg
        self.data = data

    def view(self):
        logging.warning(f"\n\nMaster: {self.master}\nMessage: {self.msg}\nData: {self.data}\n\n")

    def getJson(self):
        return {'master': self.master, 'msg': self.msg, 'data': self.data}

    def loadJson(self, rawData):
        decodedData = rawData.decode('ASCII')
        obj = json.loads(decodedData)           #returns an object from a string representing a json object.
        self.master = obj['master']
        self.msg = obj['msg']
        self.data = obj['data']

    def dumpJson(self):
        rawData = json.dumps(self.getJson())    #returns a string representing a json object from an object.
        return rawData.encode('ASCII')


EXPECTED_SIZE = 323893
EXPECTED_NAME = "ChromeSetup0-323892.spld"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
clientList = [s.getsockname()[0], '192.168.1.2', '192.168.1.3','192.162.1.4']
url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B2A0BAEDD-4834-F37C-6BB6-2BD8AA910DF4%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DCHBD%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'

clientIpSegmentMap= {s.getsockname()[0]: '0-323892', '192.168.1.2': '323893-647785', '192.168.1.3': '647786-971678', '192.162.1.4': '971679-1295575'}
distributionMsg = MSG( {"fileLink": url, "clientIpSegmentMap": clientIpSegmentMap, "filenameWithExt" : "ChromeSetup.exe"}, "Distribution message", False)

responseTuple = getFileDetails(s.getsockname()[0],distributionMsg,s,False)


if(responseTuple[0]==EXPECTED_NAME and responseTuple[1]==EXPECTED_SIZE):
    print("\n\nPassed!\nActual name: "+responseTuple[0]+" Expected name: "+EXPECTED_NAME+"\nActual FileSize: "+str(responseTuple[1])+" Expected FileSize: "+str(EXPECTED_SIZE)+"\nActual FileLink: "+url+" Expected FileLink: "+url)
else:
    print("Test Failed")




