from BackEnd import BackEnd
import json

class BackEndJsonCallback(BackEnd):
    
    def on_read(self, data):
        data = self.__unwrapData(data)
        return BackEnd.on_read(self, data)
        
    def write(self, data):
        data = self.__wrapData(data)
        return BackEnd.write(self, data)
        
        
    def __wrapData(self, data):
        return json.dumps(data)
    
    def __unwrapData(self, data):
        return json.loads(data)