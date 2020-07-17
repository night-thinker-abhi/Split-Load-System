import requests
import socket
import os
import sys
sys.path.append('../../')
from services.divideFile import divideFile


EXPECTED_SEGMENT = "0-323892"
EXPECTED_NAME = "ChromeSetup.exe"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
clientList = [s.getsockname()[0], '192.168.1.2', '192.168.1.3','192.162.1.4']
url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B2A0BAEDD-4834-F37C-6BB6-2BD8AA910DF4%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DCHBD%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'

responseTuple = divideFile(url,clientList)
clientFileSection=responseTuple[0]
filename = responseTuple[1]

if(clientFileSection[s.getsockname()[0]]==EXPECTED_SEGMENT and filename==EXPECTED_NAME):
    print("\n\nPassed!\nActual Segment: "+clientFileSection[s.getsockname()[0]]+" Expected Segment: "+EXPECTED_SEGMENT+"\nActual Name: "+filename+" Expected Name: "+EXPECTED_NAME)
else:
    print("Test Failed")




