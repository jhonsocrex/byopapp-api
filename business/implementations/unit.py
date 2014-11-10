
class Listing():  
    
    def __init__(self, MONGO_URL, MONGO_DB, myDB, db):
        self.__MONGO_URL__ = MONGO_URL
        self.__MONGO_DB__ = MONGO_DB
        self.__myDBL__ = myDB
        self.__db__ = db

    def GetNearestNeighborhoodByCordinates(self, latitude, longitude):
        geoPoint = []
        
    
    def PairListingNeighborhood(self):
        listingsCollection = self.__db__['listings']
        neighborhoodCollection = self.__db__['neighborhood']
	    
	    # filter the listting that iths neiborhood have not been updated
	    filtersDic = {neighborhood = None
	    filteredListingsCursors = listingsCollection.find(filtersDic)
	    
	    # returns the list of data objects
		filteredListingsList = list(filteredListingsCursors)
	    
	    # uldate those listings
		filteredListingsCursors = listingsCollection.find(filtersDic, { "body": 0, "title":0 , "description":0, "feetype":0})
		
        