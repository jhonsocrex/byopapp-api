
# mongodb
from pymongo import MongoClient
from bson.objectid import ObjectId

class Listings():
    
    def __init__(self, db):
        self.__collectionName__ = "listingoptions"
        self.__db__ = db
        self.__loadConnection()
    
    def __loadConnection(self):
        self.__collectionObject__ = self.__db__[self.__collectionName__]
    
    def getLandLordEmailByListingId(self , listingid):
        landlordEmail = ""
        # missing email field in the database: the crawler must pull that info
        #landlordEmail = self.__collectionObject__.find_one({'_id': ObjectId(listingid)} )
        landlordEmail = "jhonjairoroa87@gmail.com"
        return landlordEmail