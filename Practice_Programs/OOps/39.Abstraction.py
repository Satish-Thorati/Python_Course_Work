#39. Abstract Database Connector


from abc import ABC, abstractmethod

class DBConnector(ABC):
   @abstractmethod
   def connect(self):
       pass

class MySQLConnector(DBConnector):
    def connect(self):
       print("Connected to MySQL")

db = MySQLConnector()
db.connect()