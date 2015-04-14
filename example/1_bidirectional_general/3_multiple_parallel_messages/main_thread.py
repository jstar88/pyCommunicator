from pyCommunicator.FrontEnd import FrontEnd

def onRead(output):
    print 'got '+output

c = FrontEnd(['python','ext_service.py'])
c.onRead += onRead
c.run()

d = FrontEnd(['python','ext_service.py'])
d.onRead += onRead
d.run()

c.write('command1')
d.write('command2')

print 'end'

''' print:

end
got command2
got command1

'''


''' note:
This time we created more inline connections to the same file:
command2 will run in a different connection so it doesn't wait for command1
'''