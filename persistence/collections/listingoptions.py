
# mongodb
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

class ListingOptions():
    
    def __init__(self, db):
        self.__collectionName__ = "listingoptions"
        self.__db__ = db
        self.__loadConnection()
    
    def __loadConnection(self):
        self.__collectionObject__ = self.__db__[self.__collectionName__]

    def saveListingOptionClick(self , listingid, useremail, optionname):
        returnSuccess = True
        objToInsert = {
            "listingId": listingid,
            "useremail": useremail,
            "optionname": optionname,
            "createdat" : datetime.datetime.now()
        }
        self.__collectionObject__.insert(objToInsert)
        return returnSuccess