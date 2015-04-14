# pyCommunicator
Library to make asynchronous-statefull-bidirectional communication with external software. 


This is the most complex example, you can find easier examples in this project 


```python
     
    from pyCommunicator.FrontEndMarshalCallback import FrontEndMarshalCallback

    #function called when output of the first command is ready
    def onRead1(output):
        print "1 " +  str(output)

    #function called when output of the second command is ready
    def onRead2(output):
        print "2 " + str(output)
    
    #function called when output of the third command is ready
    def onRead3(output):
        print "3 " + str(output)
        
    #the cmd command
    cmd  = ['python','ext_service_marshal_callback.py']

    #create a new communication channel between this and an external python file
    # multiple requests from c channel will be enqueued and processed inline
    c = FrontEndMarshalCallback(cmd)
    c.run()
    
    #create a new communication channel between this and an external python file
    # multiple requests from d channel will be enqueued and processed inline
    d = FrontEndMarshalCallback(cmd)
    d.run()

    #messages are any type of python's primitive data.
    msg1 = ["Hello",'World','1']
    msg2 = ["Hello",'World','2']
    msg3 = ["Hello",'World','3']

    # start sending array messages to the target file through 2 channels 
    c.write(msg1,onRead1)
    c.write(msg2,onRead2)
    d.write(msg3,onRead3)
    
    # show the not-blocking system
    print 'END'


    ''' print:

    'END'
    3 ['Hello', 'World', '3']
    1 ['Hello', 'World', '1']
    2 ['Hello', 'World', '2']

    '''
```

