from pyCommunicator.FrontEndJsonCallback import FrontEndJsonCallback

def onRead1(output):
    print "1 " +  str(output)

def onRead2(output):
    print "2 " + str(output)
    
def onRead3(output):
    print "3 " + str(output)

c = FrontEndJsonCallback(['python','ext_service_marshal_callback.py'])
c.run()
d = FrontEndJsonCallback(['python','ext_service_marshal_callback.py'])
d.run()


c.write(["Hello",'World','1'],onRead1)
c.write(["Hello",'World','2'],onRead2)
d.write(["Hello",'World','3'],onRead3)


''' print:

3 ['Hello', 'World', '3']
1 ['Hello', 'World', '1']
2 ['Hello', 'World', '2']

'''