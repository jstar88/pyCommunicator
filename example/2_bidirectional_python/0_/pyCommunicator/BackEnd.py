import Event
import threading
import sys

class BackEnd(object):
    onRead = Event.Event()
    
    def __init__(self):
        pass
    
    def run(self):
        def rund():
            while True:
                self.on_read(raw_input())
            
        t = threading.Thread(target=rund)
        t.start()
        
    def write(self,data):
        print data
        sys.stdout.flush()
        
    def on_read(self,data):
        return self.onRead(data)