from pyCommunicator.FrontEnd import FrontEnd

def onRead(output):
    print 'got '+output

c = FrontEnd(['python','ext_service.py'])
c.onRead += onRead
c.run()

c.write('command1')
c.write('command2')

print 'end'

''' print:

end
got command1
got command2

'''

''' note:
even if the sytem is not-blocking, all the messages are enqueued and processed
inline:
command1 require more time to be processed but command2 will wait it.
This is very usefull for critical communication like a database

'''