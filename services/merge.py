import os

def merge(distributionMsg):
    fileString = ''
    filenameWithExt = distributionMsg.data['filenameWithExt']
    filename = filenameWithExt.split('.')[0]
    for segment in distributionMsg.data['clientIpSegmentMap'].values():
	    fileString = fileString + filename + segment + '.spld' + ' + '
    fileString = fileString[:-2]
    distributionMsg.data['clientIpSegmentMap'].values()
    os.system(f'copy /b {fileString} {filenameWithExt}')
    print("Files merged")
    # if(os.system(f'copy /b {regexFile}* {filename}')):
    os.system(f'del {filename}*.spld')
