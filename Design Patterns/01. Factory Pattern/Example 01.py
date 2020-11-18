from abc import ABC, abstractmethod


class DBManager(ABC):
    
    @abstractmethod
    def connection(self):
        pass


class SQLServer(DBManager):
    
    def connection(self):
        return ('Microsoft Database Connected')
    

class Oracle(DBManager):
    
    def connection(self):
        return ('Oracle Database Connected')


class MariaDB(DBManager):
    
    def connection(self):
        return ('Maria Database Connected')
    

class DBConnectFactory:
    
    def getDBConnection(self, DB):
        return DB.connection()
    
    

db_factory = DBConnectFactory()

print(db_factory.getDBConnection(SQLServer()))
print(db_factory.getDBConnection(Oracle()))
print(db_factory.getDBConnection(MariaDB()))
