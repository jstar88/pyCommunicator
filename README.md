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
   from pyCommunicator.Communicator import Communicator
   
   def callback(v):
     print v
   
   communicator = Communicator()
   communicator.addRequest(['python', 'test.py'], 'a simple message string', callback)
```

### PyPyCommunicator.py
