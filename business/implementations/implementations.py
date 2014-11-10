
from persistence.mongodatabase import mongoDatabase
from pymongo import MongoClient

from business.utils.mailsender import MailSender

from persistence.collections.listings import Listings
from persistence.collections.listingoptions import ListingOptions

class Implementations():
    
    def __init__(self):
 
        # load constants
        self.__MONGO_URL__ = "mongodb://jhon:1234@kahana.mongohq.com:10066/app30172457"
        self.__MONGO_DB__ = "app30172457"

        # init db connection
        self.__myDB__ = mongoDatabase(self.__MONGO_URL__)
        self.__db__ = self.__myDB__.getDB(self.__MONGO_DB__)
    
    def sendEmailToContact(self, listingid= None, useremail=None ):
        returnSuccess = False
        
        if listingid is not None and useremail is not None:
    		
    		listingCollection = Listings(self.__db__)
    		# get landlord email
    		landLordEmail = listingCollection.getLandLordEmailByListingId(listingid)
    		## instantiate email sender object
        	mailSenderObj = MailSender('smtp.gmail.com', 587, 'jhon@socrex.com' , '123456789@Socrex')
        	## send email
	        mailSenderObj.sendEmail(useremail,landLordEmail,'subject test' , 'subject body')
	        ## email quit sender object
	        mailSenderObj.quit()
	        
	        # save hit in the listing option collection
	        listingOptionCollection = ListingOptions(self.__db__)
	        listingOptionCollection.saveListingOptionClick(listingid,useremail,"contact")
	        
	        ## add ok code to dto
	        returnSuccess = True
	        
        return returnSuccess

    def sendEmailConcierge(self, email, username, userphone, listing_url, listingid):
        returnSuccess = False
        
        if email is not None and username is not None and userphone is not None and listing_url is not None and listingid is not None:
            
            listingCollection = Listings(self.__db__)

            subject = str(username) + " - " + str(listingid)
            body = "User: " + username + "<br> Email: " + email + "<br> Phone: "+userphone+"<br> Url: <a href=\""+listing_url+"\">"+listing_url+"</a>"
            # get landlord email
            ## instantiate email sender object
            mailSenderObj = MailSender('smtp.gmail.com', 587, 'concierge@socrex.com', 'monaco123')
            ## send email
            mailSenderObj.sendEmail('concierge@socrex.com', 'concierge@socrex.com', subject , body)
            ## email quit sender object
            mailSenderObj.quit()
            
            # save hit in the listing option collection
            # listingOptionCollection = ListingOptions(self.__db__)
            # listingOptionCollection.saveListingOptionClick(listingid,useremail,"contact")
            
            ## add ok code to dto
            returnSuccess = True
            
        return returnSuccess
    
    def verifyListingAvailability(self, listingid= None, useremail=None ):
        returnSuccess = False
        
        if listingid is not None and useremail is not None:
	        
	        # save hit in the listing option collection
	        listingOptionCollection = ListingOptions(self.__db__)
	        listingOptionCollection.saveListingOptionClick(listingid,useremail,"verifyavailability")
	        
	        returnSuccess = True
	        
        return returnSuccess
    
    def expertReview(self, listingid= None, useremail=None ):
        returnSuccess = False
        
        if listingid is not None and useremail is not None:
	        
	        # save hit in the listing option collection
	        listingOptionCollection = ListingOptions(self.__db__)
	        listingOptionCollection.saveListingOptionClick(listingid,useremail,"expertreview")
	        
	        returnSuccess = True
	        
        return returnSuccess
    
    def virtualTour(self, listingid= None, useremail=None ):
        returnSuccess = False
        
        if listingid is not None and useremail is not None:
	        
	        # save hit in the listing option collection
	        listingOptionCollection = ListingOptions(self.__db__)
	        listingOptionCollection.saveListingOptionClick(listingid,useremail,"virtualtour")
	        
	        returnSuccess = True
	        
        return returnSuccess

    def listingDetails(self, listingid= None):
        returnSuccess = False
        
        if listingid is not None:
            
            # save hit in the listing option collection
            listingOptionCollection = ListingOptions(self.__db__)
            #listingOptionCollection.saveListingOptionClick(listingid,useremail,"listingdetails")
            
            returnSuccess = True
            
        return returnSuccess

    def originalListing(self, listingid= None, useremail=None ):
        returnSuccess = False
        
        if listingid is not None and useremail is not None:
            
            # save hit in the listing option collection
            listingOptionCollection = ListingOptions(self.__db__)
            listingOptionCollection.saveListingOptionClick(listingid,useremail,"originallisting")
            
            returnSuccess = True
            
        return returnSuccess
        
        