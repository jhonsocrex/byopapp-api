
# mongodb
from pymongo import MongoClient

class mongoDatabase():
    
    def __init__(self , databaseURL):
        self.__databaseUrl__ = databaseURL 
        self.connectToMongoDatabase(self.__databaseUrl__)
    
    def connectToMongoDatabase(self , databaseURL):
        self.__mongoClient__ = MongoClient(databaseURL)

    def getDB(self , dbName):
        return self.__mongoClient__[dbName]