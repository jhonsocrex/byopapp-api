import smtplib

class MailSender():  
    
    def __init__(self, host,port, user, password):
        self.__host__ = host
        self.__port__ = port
        self.__user__ = user
        self.__password__ = password
        self.__initSMTPObject()
    
    # initialize SMTP object
    def __initSMTPObject(self):
        self.__smtpObj__  = smtplib.SMTP(self.__host__, self.__port__)
        self.__smtpObj__.ehlo()
        self.__smtpObj__.starttls()
        self.__smtpObj__.login(self.__user__, self.__password__)
        
    def sendEmail(self,sender,recipient, subject, body):
        headerAndBody = self.__buildEmail(sender, recipient, subject , body)
        self.__smtpObj__.sendmail(sender, recipient, headerAndBody)
        
    def __buildEmail(self, sender, recipient, subject , body):
        
        headers = [
            "From: " + sender,
            "Subject: " + subject,
            "To: " + recipient,
            "MIME-Version: 1.0",
            "Content-Type: text/html"
        ]
        headers = "\r\n".join(headers)
        
        headerAndBody = headers + "\r\n\r\n" + body
        return headerAndBody
    
    def quit(self):
        self.__smtpObj__.quit()
        
