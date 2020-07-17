import logging

FORMAT = '[%(asctime)-15s] {%(filename)s} {%(funcName)s} {%(lineno)d} %(message)s'
logging.basicConfig(format=FORMAT, level=logging.WARNING)

def getFileDetails(OWNIP,distributionMsg,socket,flag=True):
	laddr= socket.getsockname()[0]
	raddr = socket.getpeername()[0]
	if flag:
		addr = laddr if laddr!=OWNIP else raddr
		
	else:
		addr = laddr if laddr==OWNIP else raddr
	segment = distributionMsg.data["clientIpSegmentMap"][addr].split("-")
	fileSize = int(segment[1])-int(segment[0])+1
	# logging.warning(f'{segment[1]} - {segment[0]} + 1 = {fileSize}')
	filenameWithExt = distributionMsg.data['filenameWithExt']
	fileName = filenameWithExt.split('.')[0] + str(distributionMsg.data["clientIpSegmentMap"][addr])+".spld"
	return (fileName,fileSize)
	