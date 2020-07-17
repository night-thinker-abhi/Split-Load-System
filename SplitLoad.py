import threading
import time
import socket
import struct
import json
import sys
from services.portServices import get_free_tcp_port
from services.divideFile import divideFile
from services.startDownload import startDownload
from services.getOwnIp import getOwnIp
from services.sendFile import sendFile
from services.recvFile import recvFile
from services.getFileDetails import getFileDetails
from services.merge import merge
from ui import ds1
from ui import ds2
from ui import ds3
from ui import ds4
from ui import ds5
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import logging
from time import sleep
from random import random
import os
import enlighten

fileLink = "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B2A0BAEDD-4834-F37C-6BB6-2BD8AA910DF4%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DCHBD%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
appendLock = threading.Lock()
segmentsFetched = False
choice = -1
ui1 = "abc"
ui2 = "abc"
ui3 = "abc"
ui4 = None
ui5 = None
Form = "abc"
Form2 = None
Form4 = None
Form5 = None
app = "abc"
isMaster = False
isBusy = False  # Tell whether the this system is already busy in some download or not
BUFSIZE = 655350
broadcastPort = 2100
tcpPort = 8888
clientsIp = []  # list to store clients
tcpConnectionList = []
broadcastInterface = "192.168.43.255"
broadcastListenInterface = "0.0.0.0"
ipSockMap = {}
ipThreadMap = {}
ipPortMap = {}
clientFileSection = {}
clientIpSegmentMap = {}
OWNPORT = get_free_tcp_port()
OWNIP = getOwnIp()   
clientIpList=[]
FORMAT = '[%(asctime)-15s] {%(filename)s} {%(funcName)s} {%(lineno)d} %(message)s'
logging.basicConfig(format=FORMAT, level=logging.WARNING)

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

distributionMsg = MSG({})

def listenClientTcpReq(arg):
    global clientIpList
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (OWNIP, tcpPort)
    tcpSock.bind(serverAddress)
    totalClients = len(clientIpList)
    tcpSock.listen(totalClients)
    while(len(ipSockMap.keys())<totalClients):    
        connection, address = tcpSock.accept()
        #logging.warning(f'Accepted connection: {connection}')
        if address[0] not in ipSockMap:
            ipSockMap[address[0]]=connection
        #logging.warning(f'Connected to client(Inside listenClientTcpReq): {address[0]}, {address[1]}')
        #logging.warning(f"ipSockMap.keys(): {len(ipSockMap.keys())}  totalClients:  {totalClients}")
        if len(ipSockMap.keys())==totalClients:
            #logging.warning("All clients connected")
            break
    #logging.warning("Exiting listenClientTcpReq")

 
def initiateDownload(args):
    segment = args[0]
    fileLink = args[1]
    filenameWithExt = args[2]
    startDownload(segment, fileLink, filenameWithExt)
    #logging.warning("Exiting initiateDownload")

def listenBroadcast(arg):  # client
    global clientIpList
    data = address = None
    manager = enlighten.get_manager()
    #logging.warning("listening broadcast started")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((broadcastListenInterface, broadcastPort))
    res = MSG({})
    #logging.warning('Listening for master at {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(BUFSIZE)
    res.loadJson(data)
    sock.close()
    if res.msg == 'Add request':
        tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.warning("Announcement Received")
        logging.warning("Making connection with the Master at IP = {} and Port = {}".format(
            address[0], tcpPort))
        tcpServerAddress = (address[0], tcpPort)
        tcpSock.connect(tcpServerAddress)
        rawData = tcpSock.recv(BUFSIZE)
        distributionMsg = MSG({})
        distributionMsg.loadJson(rawData)
        #logging.warning("distribution message received ")
        clientDownloadStarted()
        
        distributionMsg.view()
        filenameWithExt = distributionMsg.data['filenameWithExt']
        clientIpSegmentMap = distributionMsg.data['clientIpSegmentMap']
        size = int(list(clientIpSegmentMap.values())[len(list(clientIpSegmentMap.values()))-1].split('-')[1]) + 1
        setFilename(filenameWithExt, size)
        segment = clientIpSegmentMap[OWNIP]
        #logging.warning (segment)
        fileLink = distributionMsg.data['fileLink']
        ipSockMap[address[0]] = tcpSock
        ipSockMap[OWNIP] = None
        clientIpList = distributionMsg.data['clientIpSegmentMap'].keys()
        listenClientTcpReqThread = threading.Thread(target=listenClientTcpReq, args = ("",))
        listenClientTcpReqThread.start()

        recvFileThread = None
        sleep(random()*10)
        for client in clientIpList:
            if client not in ipSockMap:
                tcpServerAddress = (client, tcpPort)
                tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcpSock.connect(tcpServerAddress)
                #logging.warning(f'Requested connection: {tcpSock}')  
                ipSockMap[client]=tcpSock

        threads = []
        progressBars = {}

        for client in ipSockMap:
            if(client != OWNIP):
                tcpSock = ipSockMap[client]
                filedetails = getFileDetails(OWNIP, distributionMsg, tcpSock)
                recvFileProgress = manager.counter(total= filedetails[1], desc="Receiving File", unit="bytes", color="green")
                progressBars[client] = (recvFileProgress,filedetails)

        for client in ipSockMap:
            if(client != OWNIP):
                tcpSock = ipSockMap[client]
                recvFileThread = threading.Thread(target=recvFile,args=((tcpSock, progressBars[client][1][0], progressBars[client][1][1], progressBars[client][0]),))
                recvFileThread.start()
                threads.append(recvFileThread)

        # for x in ipSockMap:
            #logging.warning(x)

        startTime = time.time()
        initiateDownloadThread = threading.Thread(
            target=initiateDownload, args=((segment, fileLink, filenameWithExt),))  # Download Started
        initiateDownloadThread.start()
        threads.append(initiateDownloadThread)
        
        
        filename = filenameWithExt.split('.')[0] + str(segment) +'.spld'

        progressBars = {}

        for client in ipSockMap:
            if(client != OWNIP):
                tcpSock = ipSockMap[client]
                filedetails = getFileDetails(OWNIP, distributionMsg, tcpSock, flag = False)
                sendFileProgress = manager.counter(total=filedetails[1], desc=f"Sending File", unit="bytes", color="red")
                progressBars[client] = (sendFileProgress,filedetails)

        for ipSock in ipSockMap:
            client = ipSock
            if client != OWNIP:
                tcpSock = ipSockMap[client] 
                sendFileThread = threading.Thread(target=sendFile,args=((tcpSock, progressBars[client][1][0], progressBars[client][1][1], progressBars[client][0]),))
                sendFileThread.start()
                threads.append(sendFileThread)

        for thread in threads:
            thread.join()
        #logging.warning("Out of all Send and Recv Threads.")
 
        
        regexFile = filenameWithExt.split('.')[0]
        merge(distributionMsg)
        #logging.warning(f"Downloading time : {time.time() - startTime}")
        downloadComplete()
        # tcpSock.close()
        logging.warning("listening to master ended")


def announceBroadcast(arg):
    global choice
    #logging.warning("announcing broadcast started")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while(True):
        res = MSG({}, "Add request", isMaster)
        sock.sendto(res.dumpJson(), (broadcastInterface, broadcastPort))
        logging.warning("Announcing to Join.")
        time.sleep(1)
        # for i in clientsIp:
            #logging.warning(f"ip: {i}")
        #logging.warning("enter 1 for reannounce or 0 to end announcement")
        # refreshList()
        while(choice == -1):
            pass
        if(choice == 0):
            res.msg = 'Broadcast Ends'
            # sock.sendto(res.dumpJson(), (broadcastInterface, broadcastPort))
            tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpServerAddress = (OWNIP, tcpPort)
            tcpSock.connect(tcpServerAddress)
            break
        choice = -1
    sock.close()
    #logging.warning("announcing broadcast ended")

def sendDistributionMsg(args):
    global segmentsFetched
    global distributionMsg
    connection = args[0]
    connection.sendall(distributionMsg.dumpJson())
    #logging.warning("Exiting sendDistributionMsg")

def listenTcp(arg):
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (OWNIP, tcpPort)
    tcpSock.bind(serverAddress)
    tcpSock.listen(10)
    while(True):    
        connection, address = tcpSock.accept()
        if connection.getsockname()[0] == connection.getpeername()[0]:
            break
        tcpConnectionList.append((connection, address))
        clientsIp.append(address[0])
        ipSockMap[address[0]] = connection
        # refreshList()
        #logging.warning(f'Connected to : {address[0]} : {address[1]}')
    #logging.warning("Exiting listenTcp thread.")

def Master(arg):
    startMasterScreen()
    global isMaster
    isMaster = True
    manager = enlighten.get_manager()
    
    listenTcpThread = threading.Thread(target=listenTcp, args = ("",))
    listenTcpThread.start()
    announceBroadcastThread = threading.Thread(
        target=announceBroadcast, args=("",))
    announceBroadcastThread.start()
    announceBroadcastThread.join()
    # while(announceBroadcastThread.is_alive()):
    #     pass

    # if got all the clients, Time to distribute the file and send it to others
    # if not announceBroadcastThread.is_alive():
    global segmentsFetched
    global distributionMsg
    clientsIp.append(OWNIP)
    clientIpSegmentMap, filenameWithExt, size = divideFile(fileLink, clientsIp)
    distributionMsg = MSG(
        {"fileLink": fileLink, "clientIpSegmentMap": clientIpSegmentMap, "filenameWithExt" : filenameWithExt}, "Distribution message", isMaster)
    #logging.warning("This is the distribution msg ")
    distributionMsg.view()
    setFilename(filenameWithExt, int(size))
    for element in tcpConnectionList:
        sendDistributionMsgThread = threading.Thread(target = sendDistributionMsg, args = ((element[0],element[1]),))
        sendDistributionMsgThread.start()
 
            
    segmentsFetched = True
    segment = clientIpSegmentMap[OWNIP]

    threads = []
    progressBars = {}

    for client in ipSockMap:
        if(client != OWNIP):
            tcpSock = ipSockMap[client]
            filedetails = getFileDetails(OWNIP, distributionMsg, tcpSock)
            recvFileProgress = manager.counter(total= filedetails[1], desc="Receiving File", unit="bytes", color="green")
            progressBars[client] = (recvFileProgress,filedetails)
            # logging.warning(f"Client : {client}")

    for client in ipSockMap:
        if(client != OWNIP):
            tcpSock = ipSockMap[client]
            recvFileThread = threading.Thread(target=recvFile,args=((tcpSock, progressBars[client][1][0], progressBars[client][1][1], progressBars[client][0]),))
            recvFileThread.start()
            threads.append(recvFileThread)

    startTime = time.time()
    initiateDownloadThread = threading.Thread(target=initiateDownload, args=(
        (segment, fileLink, filenameWithExt),))  # Download Started in Master
    initiateDownloadThread.start()
    threads.append(initiateDownloadThread)

    segment = clientIpSegmentMap[OWNIP]
    filename = filenameWithExt.split('.')[0] + str(segment) + '.spld'

    progressBars = {}

    for client in ipSockMap:
        if(client != OWNIP):
            tcpSock = ipSockMap[client]
            filedetails = getFileDetails(OWNIP, distributionMsg, tcpSock, flag = False)
            sendFileProgress = manager.counter(total=filedetails[1], desc=f"Sending File", unit="bytes", color="red")
            progressBars[client] = (sendFileProgress,filedetails)

    for ipSock in ipSockMap:
        client = ipSock
        if client != OWNIP:
            tcpSock = ipSockMap[client] 
            sendFileThread = threading.Thread(target=sendFile,args=((tcpSock, progressBars[client][1][0], progressBars[client][1][1], progressBars[client][0]),))
            sendFileThread.start()
            threads.append(sendFileThread)

    #logging.warning("recvFileThread joined")
    for thread in threads:
        thread.join()

    regexFile = filenameWithExt.split('.')[0]
    merge(distributionMsg)
    #logging.warning(f"Downloading time : {time.time() - startTime}")
    downloadComplete()
    #logging.warning("Exiting Master")

def Client():
    listenBroadcastThread = threading.Thread(
        target=listenBroadcast, args=("",))
    listenBroadcastThread.start()
    Form.close()
    ui5.changeText("Waiting",'red')
    Form5.show()
    ui5.label_3.setVisible(False)
    ui5.label_4.setVisible(False)

    # listenBroadcastThread.join()
def clientDownloadStarted():
    ui5.changeText("Downloading")
    ui5.label_3.setVisible(True)
    

def startMasterScreen():
    global app
    global Form2
    global Form

def checkClientList(args):
    global clientsIp
    global choice
    #logging.warning("CheckClientList called")
    length = 0
    while(choice != 0):
        # #logging.warning(f'{len(clientsIp)}')
        sleep(1)
        if(length != len(clientsIp)):
            length = len(clientsIp)
            #logging.warning("Refreshing List")
            refreshList()
    #logging.warning("Exiting checkClientList")
        

def startMasterUtil():
    #logging.warning("Master")
    masterThread = threading.Thread(target=Master, args=('',))
    masterThread.start()
    checkClientListThread = threading.Thread(target=checkClientList, args=('',))
    checkClientListThread.start()
    Form.close()
    Form2.show()
    refreshList()

def reannounce():
    global choice
    choice = 1
    refreshList()

def setFilename(filenameWithExt, size:int):
    sizeString = ''
    if ((size // 2**30) > 0):
        sizeString = ' GB'
        sizeString = '%.3f' %(size / 2**30) + sizeString
    elif ((size // 2**20) > 0):
        sizeString = ' MB'
        sizeString = '%.3f' %(size / 2**20) + sizeString
    else:
        sizeString = ' KB'
        sizeString = '%.3f' %(size / 2**10) + sizeString

    fileString = f"File Name : {filenameWithExt} ({sizeString})"
    ui5.changeTextFilename(fileString)

def refreshList():
    global clientsIp
    model = QtGui.QStandardItemModel()
    ui2.listView.setModel(model)

    for i in clientsIp:
        item = QtGui.QStandardItem(i)
        model.appendRow(item)


def endAnnounceMent():
    global choice
    global fileLink
    fileLink = str(ui4.downloadLink.toPlainText())
    fileLink = fileLink.strip()
    choice = 0
    Form4.close()
    Form5.show()
    ui5.label_4.setVisible(False)


def urlPicker():
    Form2.close()
    Form4.show()

def downloadComplete():
    ui5.changeText("Download Complete",'green')
    ui5.label_2.setVisible(False)
    path = os.path.dirname(os.path.abspath(__file__))
    path = "File downloaded at : " + path
    ui5.label_4.setVisible(True)
    ui5.changeTextDownloadedAt(path)
    # # setDownloadedAt()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui1 = ds1.Ui_Form()
    ui1.setupUi(Form)
    Form2 = QtWidgets.QWidget()
    ui2 = ds2.Ui_Form()
    ui2.setupUi(Form2)

    Form4 = QtWidgets.QWidget()
    ui4 = ds4.Ui_Form()
    ui4.setupUi(Form4)

    Form5 = QtWidgets.QWidget()
    ui5 = ds5.Ui_Form()
    ui5.setupUi(Form5)

    ui1.Master.clicked.connect(startMasterUtil)
    ui1.Client.clicked.connect(Client)
    ui2.Refresh.clicked.connect(reannounce)
    ui2.Next.clicked.connect(urlPicker)

    ui4.Download.clicked.connect(endAnnounceMent)
    Form.show()
    sys.exit(app.exec_())
    # while(True):
    #     pass
