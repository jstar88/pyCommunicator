from pyCommunicator.FrontEndJsonCallback import FrontEndJsonCallback
from DBStub import DBStub


def showResults(data):
    print 'got '+str(data)

f = FrontEndJsonCallback(['service\dist\generic_instance_manager.exe'])
f.run()

db = DBStub(f,'my.db','objects',showResults)
db.addObject([1,2,3],'first','mypath',showResults)
db.getAllObjects(showResults)