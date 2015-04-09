# pyCommunicator
Library to make asynchronous-statefull-bidirectional communication with external software.  

### Communicator.py
Provide the communication layer between python and any other software.  
Public methods are  
* self.**addRequest**(command, message, callback)
* self.**addFreeRequest**(command, message, callback)

where   

1. **command** = array rappresenting the cmd command
2. **message** = string that will be sent to stdin of target file
3. **callback** = callable function called when returns are ready(stdout of target file)

for example, to call another python file "test.py" and output its result:

```python
    #main.py
    from pyCommunicator.Communicator import Communicator
   
    def callback(v):
       print v   # print 'a simple message string'
   
    communicator = Communicator()
    communicator.addRequest(['python', 'test.py'], 'a simple message string', callback)
```

```python
    #test.py
    import sys
    print sys.stdin.readline()
```


### PyPyCommunicator.py
Provide the communication layer between python and another python file.   
It work like Communicator.py with the exception that message will be dump by marshal module and the callback return will be loaded by marshal module too.  

Public methods are  
* self.**addRequest**(command, message, callback)
* self.**addFreeRequest**(command, message, callback)

where   

1. **command** = array rappresenting the cmd command
2. **message** = any python base object that will be sent as marshal string to target file
3. **callback** = callable function called when returns are ready(stdout of target file)

for example, to call another python file "test.py" and output its result:

```python
    #main.py
    from pyCommunicator.PyPyCommunicator import PyPyCommunicator
   
    def callback(v):
       print v   # print [1,2,3]
   
    communicator = PyPyCommunicator()
    communicator.addRequest(['python', 'test.py'], [1,2,3], callback)
```

```python
    #test.py
    import marshal
    import sys

    def reply(data):
       print marshal.dumps(data)
    
    def retriveData():
       return marshal.loads(sys.stdin.readline())

    reply(retriveData())
```

### addRequest vs addFreeRequest
Both functions call a callback when the result is ready, so they will not block your main code.   

*addFreeRequest*: this methond create a new thread where the communication run
*addRequest*: here, instead, the request is enqueued so it will be processed only when all the older requests are ended  


*addRequest* is ideal for critical communications, like with a database, where the order between requests must be respected.   
*addFreeRequest* in the other hand, will ignore any other request and so it's best suited for hight performance
