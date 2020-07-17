import os
import logging
from time import sleep
from alive_progress import alive_bar

BUFFER_SIZE = 655350
SEPARATOR = "<SEPARATOR>"
FORMAT = '[%(asctime)-15s] {%(filename)s} {%(funcName)s} {%(lineno)d} %(message)s'
logging.basicConfig(format=FORMAT, level=logging.WARNING)

def sendFile(args):
    # logging.warning("Starting sendFile")
    tcpSock = args[0]
    filename = args[1]
    filesize = args[2]
    # logging.warning(f"\nSending: {filename} to {tcpSock}\n")
    # logging.warning(f"Filesize : {filesize}")
    while(True):
        try:
            f = open(filename, "rb")
            break
        except Exception as e:
            pass
    l=0
    byte_read=f.read(BUFFER_SIZE)
    if byte_read:
        l = len(byte_read)
    print("\n\n")
    with alive_bar(filesize, manual = True) as bar:
        while(True):
            while(not byte_read and f.tell()<filesize):
                byte_read = f.read(BUFFER_SIZE)
                bar(perc=f.tell()/filesize, text='Sending File')
            if(byte_read):
                tcpSock.sendall(byte_read)
                l=l+len(byte_read)

                # logging.warning(f"{tcpSock.getsockname()[0]} : {tcpSock.getpeername()[0]}  Length of file read: {len(byte_read)} | f.tell {f.tell()} , Total Length of file read: {l}")
                byte_read = None
                byte_read = f.read(BUFFER_SIZE)
                bar(perc=f.tell()/filesize, text='Sending File')
                # if(byte_read):
                #     logging.warning(f"{tcpSock.getsockname()[0]} : {tcpSock.getpeername()[0]} Length of file read after: {len(byte_read)}")
                # else:
                #     logging.warning(f"No Byte read.")
            else:
                break
    # logging.warning(f"Ending sendFile for {tcpSock}")
    f.close()