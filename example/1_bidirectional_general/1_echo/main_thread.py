'''
Example
Calling external echo service and write it's output
'''

from pyCommunicator.FrontEnd import FrontEnd

def onRead(output):
    print 'got '+output

c = FrontEnd(['python','ext_service.py'])
c.onRead += onRead
c.run()
c.write('command1')

print 'end'



''' print:

end
got command1

'''

''' note:
end will be the first result since the
system is not-blocking

'''