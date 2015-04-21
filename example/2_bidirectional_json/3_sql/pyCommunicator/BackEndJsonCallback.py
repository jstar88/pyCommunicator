from BackEnd import BackEnd
import json
import marshal

class BackEndJsonCallback(BackEnd):
    
    def on_read(self, data):
        data = self.__unwrapData(data)
        return BackEnd.on_read(self, data)
        
    def write(self, data):
        data = self.__wrapData(data)
        return BackEnd.write(self, data)
        
        
    def __wrapData(self, data):
        #return marshal.dumps(data)
        return json.dumps(data)
    
    def __unwrapData(self, data):
        #return marshal.loads(data)
        return json.loads(data)
    
    
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv