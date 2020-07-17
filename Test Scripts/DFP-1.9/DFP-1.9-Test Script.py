import requests
import socket
import os
import sys
import json
sys.path.append('../../')
from services.startDownload import startDownload



EXPECTED_SIZE = 323893
EXPECTED_NAME = "ChromeSetup0-323892.spld"

SEGMENT = "0-323892"
FILENAME_EXT="ChromeSetup.exe"
url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B2A0BAEDD-4834-F37C-6BB6-2BD8AA910DF4%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DCHBD%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'

startDownload(SEGMENT,url,FILENAME_EXT)

try:
    size = os.path.getsize(EXPECTED_NAME)
    if(size==EXPECTED_SIZE):
        print("\n\nPassed!\nActual name: "+EXPECTED_NAME+" Expected name: "+EXPECTED_NAME+"\nActual FileSize: "+str(size)+" Expected FileSize: "+str(EXPECTED_SIZE))
    else:
        print("Test Failed")
except Exception as e:
    print("Test Failed"+e)




