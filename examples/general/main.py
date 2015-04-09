from pyCommunicator.Communicator import Communicator

#---- define callbacks that will be called when the target file will output something ----#
def callback(v):
    print '1)' + v
    
def callback2(v):
    print '2)' + v
    
def callback3(v):
    print '3)' + v

#---- lets add some request to target files ----#
communicator = Communicator()

# we are sending the command = "python b.py" and "hello world" as stdin message. b.py contains some code to slowdown itself. 
communicator.addRequest(['python', 'b.py'], 'hello world', callback)

# Since this request is not "Free" then it will wait untill the older one(not Free) end before be processed.
communicator.addRequest(['python', 'c.py'], 'hello world2', callback2)

# This is a "Free" request, it doesn't care about olders request so it's processed fast as possibile.
communicator.addFreeRequest(['python', 'c.py'], 'hello world3', callback3)

#since the code is multithread, this will be the first output
print 'code is going to be free'

"""
code is going to be free
3)c.py
hello world3

1)b.py
hello world

2)c.py
hello world2
"""