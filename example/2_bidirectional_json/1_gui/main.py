from pyCommunicator.FrontEndJsonCallback import FrontEndJsonCallback

def guiCallback(data):
    print data

f = FrontEndJsonCallback(['python','gui.py'])
f.onRead += guiCallback
f.run()