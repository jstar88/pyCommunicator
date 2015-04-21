class DBStub:
    def __init__(self, f, dbname='example.db', tableName='objects',callback = None):
        self.constructor = {'module': 'Database', 'class':'Database', 'instance_args':[dbname]}
        self.f = f
        self.tableName = tableName
        self.__createTable('objects', ["x real", "y real", "z real", "name text", "path text"],callback)
    
    def __send(self, request, callback=None):
        self.constructor.update(request)
        self.f.write(self.constructor, callback)
    
    def __createTable(self, tableName, fields,callback=None):
        query = "CREATE TABLE IF NOT EXISTS " + tableName + " (" + ",".join(fields) + ")"
        request = {'method':'execute', 'args':[query]}
        self.__send(request,callback)
        
    def addObject(self, position, name, path,callback= None):
        x = position[0]
        y = position[1]
        z = position[2]
        query = "INSERT INTO " + self.tableName + " VALUES (?,?,?,?,?)"
        request = {'method':'execute', 'args':[query, (x, y, z, name, path)]}
        self.__send(request,callback)
        
    def removeObject(self, name,callback = None):
        query = "DELETE FROM " + self.tableName + " WHERE name=?"
        request = {'method':'execute', 'args':[query, (name)]}
        self.__send(request,callback)
        
    def clean(self, name, callback = None):
        query = "DELETE FROM " + self.tableName
        request = {'method':'execute', 'args':[query]}
        self.__send(request,callback)
        
    def getObject(self, name, callback): 
        query = 'SELECT * FROM ' + self.tableName + ' WHERE name=?'
        request = {'method':'executeFetchOne', 'args':[query, (name)]}
        self.__send(request, callback)
    
    def getAllObjects(self, callback):
        query = 'SELECT * FROM ' + self.tableName + ' ORDER BY name'
        request = {'method':'executeFetchAll', 'args':[query]}
        self.__send(request, callback)
    
    def getNearObjects(self, position, callback):
        x = position[0]
        y = position[1]
        z = position[2]
        query = 'SELECT * FROM ' + self.tableName + ' WHERE x<? AND y<? AND z<? ORDER BY name'
        request = {'method':'executeFetchAll', 'args':[query, (x, y, z)]}
        self.__send(request, callback)
