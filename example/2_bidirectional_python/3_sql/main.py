from pyCommunicator.FrontEndJsonCallback import FrontEndJsonCallback
from DBStub import DBStub


def showResults(data):
    print data

f = FrontEndJsonCallback(['service/dist/generic_instance_manager.exe'])
f.onRead += showResults
f.run()

db = DBStub(f,'my.db')
db.addObject([1,2,3],'first','mypath')
db.getAllObjects(showResults)