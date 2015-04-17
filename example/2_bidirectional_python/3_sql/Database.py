import sqlite3
class Database(object):
    
    def __init__(self, dbname):
        self.dbcon = sqlite3.connect(dbname)
        
    def execute(self,query,fields = None):
        c = self.dbcon.cursor()
        if fields is None:
            c.execute(query)
        else:
            c.execute(query,fields)
        self.dbcon.commit()
        
    def executeFetchOne(self,query,fields = None):
        c = self.dbcon.cursor()
        if fields is None:
            c.execute(query)
        else:
            c.execute(query,fields)
        self.dbcon.commit()
        return c.fetchone()
        
    def executeFetchAll(self,query,fields = None):
        c = self.dbcon.cursor()
        if fields is None:
            c.execute(query)
        else:
            c.execute(query,fields)
        self.dbcon.commit()
        return c.fetchall()
    
    def __del__(self):
        self.dbcon.close()