import requests
import socket
import os
import sys
import json
sys.path.append('../../')
from services.portServices import get_free_tcp_port

response = get_free_tcp_port()


if(response<=65536):
     print("Test Passed! Port: "+str(response))
else:
    print("Test Failed ")




