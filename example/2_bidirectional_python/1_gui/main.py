from pyCommunicator.FrontEndMarshalCallback import FrontEndMarshalCallback

def guiCallback(data):
    print data

f = FrontEndMarshalCallback(['python','gui.py'])
f.onRead += guiCallback
f.run()