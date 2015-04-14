from pyCommunicator.BackEndMarshalCallback import BackEndMarshalCallback
import time

s = BackEndMarshalCallback()
def x(data):
    if data[2] == '1':
        time.sleep(3)
    elif data[2] == '2':
        time.sleep(0)
    elif data[2] == '3':
        time.sleep(1)
    s.write(data)

s.onRead += x
s.run()