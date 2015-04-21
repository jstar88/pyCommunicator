from BackEnd import BackEnd
import json

class BackEndJsonCallback(BackEnd):
    
    def on_read(self, data):
        data = self.__unwrapData(data)
        return BackEnd.on_read(self, data)
        
    def write(self, data, hasCallback="False"):
        data = self.__wrapData(data)
        data = self.__joinData(data, hasCallback)
        return BackEnd.write(self, data)
    
    def reply(self, data):
        return self.write(data, "True")
        
    def __wrapData(self, data):
        return json.dumps(data)
    
    def __unwrapData(self, data):
        return json.loads(data)
    
    def __joinData(self, data, hasCallback):
        return hasCallback + ':' + data
