import os
import logging
import time

def startDownload(segment, fileLink, filenameWithExt):
    # url = fileLink.split('/')
    fileName = filenameWithExt.split('.')[0] + str(segment) + '.spld'
    os.system('curl -s -L  -o ' + '"' + fileName + '"' +' --range ' + segment + ' ' + '"' + fileLink +'"')
    
    # logging.warning(f"Downloading : {os.path.getsize(fileName)}")

    # os.system('curl -F 'file=fileName' http://localhost/')
