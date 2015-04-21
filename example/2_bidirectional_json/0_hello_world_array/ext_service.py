from pyCommunicator.BackEndJsonCallback import BackEndJsonCallback
import time

s = BackEndJsonCallback()
def x(data):
    if data[2] == '1':
        time.sleep(3)
    elif data[2] == '2':
        time.sleep(0)
    elif data[2] == '3':
        time.sleep(1)
    s.reply(data)

s.onRead += x
s.run()