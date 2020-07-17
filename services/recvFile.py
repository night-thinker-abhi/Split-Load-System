import os
import logging
import enlighten

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 655350
FORMAT = '[%(asctime)-15s] {%(filename)s} {%(funcName)s} {%(lineno)d} %(message)s'
logging.basicConfig(format=FORMAT, level=logging.WARNING)

def recvFile(args):
    # logging.warning("Starting recvFile")
    # logging.warning(f"args : {args}")
    tcpSock = args[0]
    filename = args[1]
    filesize = args[2]
    recvFileProgress = args[3]
    factor = 1000000
    oldFTell = 0
    # filename, filesize = getFileDetails()
    # logging.warning(f"Before Receiving at: {tcpSock}")
    # logging.warning(f"filename: {filename},  filesize: {filesize}")
    # length=0
    total = int(filesize/factor)
    # recvFileProgress = manager.counter(total= filesize, desc="Receiving File", unit="bytes", color="green")
    # recvFileProgress.update(incr=0)
    with open(filename, "wb") as f:
        # with alive_bar(filesize, manual = True) as bar:
        while (True):
            bytes_read = tcpSock.recv(BUFFER_SIZE)
            # length = length + len(bytes_read)
            # print("recv: ",length," | f.tell: ",f.tell())
            f.write(bytes_read)
            if(bytes_read):
                # updateVal = int((f.tell() - oldFTell)/factor)
                updateVal = f.tell() - oldFTell
                recvFileProgress.update(incr = updateVal)
                oldFTell = f.tell()
            if f.tell() >= filesize: 
                # logging.warning("File Received. Break")
                break
            # file_read  = file_read + len(bytes_read)
            
            # bytes_read = tcpSock.recv(BUFFER_SIZE)
        # logging.warning("File Received")
    # logging.warning(f"Ending recvFile for {tcpSock}")