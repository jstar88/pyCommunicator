from pyCommunicator.BackEnd import BackEnd
import time

s = BackEnd()
def x(data):
    if data == 'command1':
        time.sleep(3)
    elif data == 'command2':
        time.sleep(0)
    elif data == 'command3':
        time.sleep(1)
    s.write(data)
s.onRead += x
s.run()
time.sleep(10)
