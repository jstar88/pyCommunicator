'''
Simple echo service:
 capture the input and write them to output
'''

from pyCommunicator.BackEnd import BackEnd

s = BackEnd()
s.onRead += s.write
s.run()
