from FrontEnd import FrontEnd
import marshal

class FrontEndMarshalCallback(FrontEnd):
    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()
    
        def top(self):
            return self.items[self.size() - 1]

        def size(self):
            return len(self.items)
        
        def isEmpty(self):
            if self.items:
                return False
            return True
    
    def __init__(self, service):
        super(FrontEndMarshalCallback, self).__init__(service)
        self.callbacks = FrontEndMarshalCallback.Queue()
    
    def write(self, data, callback=None):
        self.callbacks.enqueue(callback)
        data = self.__wrapData(data)
        return FrontEnd.write(self, data)
        
    def on_read(self, data):
        data = self.__unwrapData(data)
        if not self.callbacks.isEmpty():
            callback = self.callbacks.dequeue()
            if callback is not None:
                callback(data)
        return FrontEnd.on_read(self, data)
    
    def __wrapData(self, data):
        return marshal.dumps(data)
    
    def __unwrapData(self, data):
        return marshal.loads(data)
