import sys 
import os 
import hashlib
import smtplib

#Python doesn't support The relative path call we should added to the system first
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils","Database.py")
sys.path.append(path)
#The 2 Lines of code above are mendatory
from models.utils.Database import Databases
class authenticates(Databases):
    def __init__(self) -> None:
        #makin inheritance from the inherited classes 
        super().__init__()
    
    def registering_User(self,data)->bool:
        #assuming we wil have the data here ,
        #TODO reformelate the data
        #TODO salt and serialize the password
        #TODO send the data to database  
        #All of those steps i encapsulated them inside the sendingData Method in Database File
        return self.sending_data(data)
        

    #if authentication done , the email will be send and the user can start using the app
    # we can add another layer of security by sending a code via email and can be verified
    def authenticate(self,email,password)->bool:
            query = {"Email":email}
            result = self.my_collect.find_one(query)
            if result:
               stored_pass = result["password"]
               stored_salt = result["salt"]
               hashed_pass = hashlib.pbkdf2_hmac("sha256",password.encode("utf-8"),stored_salt,100000)
               print(hashed_pass)
               return  stored_pass == hashed_pass
            else:
               return False
     #Less Important in case we still have Time        
    def oauth2_auth(self):
        pass     
 
    def send_emails(self):
        pass

if __name__ == "__main__":
     x = authenticates()
    #  x.sending_data(["baker","lawzi","bakricoder71@gmail.com","ArsinLupin12"])
     print(x.authenticate("bakricoder71@gmail.com","ArsinLupin12"))