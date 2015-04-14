'''
Echo service but with different process time based on command type.

'''

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

'''
note:
time.sleep(10) will emulate a long process at the creation of the communication
channel, however you will see itsn't a problem.
'''
