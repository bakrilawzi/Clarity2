import pymongo
import os
import sys
import requests,json
import mailerlite as MailerLite

path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils")
pathroot = os.path.join("C:","Users","user","Desktop","Project 308","myvenv") 
path3 = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
sys.path.append(pathroot)
sys.path.append(path)
sys.path.append(path3)
from . import user_managment
import pymongo.errors
class Databases(user_managment.mangementPass):
    def __init__(self,databaseName="Clarity",databseCollect="Users"):
        super().__init__()
        try:
           #Hiding The connection 
           connect = os.getenv("MONGO_CONNECTION")
           self.client = pymongo.MongoClient(connect)
        except pymongo.errors.ConfigurationError:
           print("an error in configuration there  the passsword is correct?") 
        #connecting to the database
        self._databaseName = databaseName
        self._collection = databseCollect
        self.db = self.client[self._databaseName]
        self.my_collect = self.db[self._collection]

    @property
    def databsseName(self):
        return self._databaseName
    
    @databsseName.setter
    def databsseName(self,value):
        try:
            if isinstance(value,str) and len(value)>0:
                self._databaseName = value
        except pymongo.errors.InvalidName:
              print("No database like this name")

    @property
    def database_Collect(self):
        return self._collection
    @database_Collect.setter
    def database_Collect(self,value):
        try:
            if isinstance(value,str) and len(value)>0:
                self._collection = value
        except pymongo.errors.InvalidName:
              print("No Collection like this name")

    def registering_Data(self,data) -> dict:
        #we took the data and converted to JSON after having encoded and salted the password for protection 
        #and enhancing security 
        if len(data) == 4:
            new_data = {}
            attributes = ["name","lastname","Email","password"]
            for idx,names in enumerate(data):
                print(names)
                if(idx==3):
                    salt,password = self.salt_Password(names)
                    new_data[attributes[idx]] = password 
                    new_data["salt"] = salt
                else:
                    new_data[attributes[idx]]  = names
            return new_data
        else:
            return {}
        

    def sending_data(self,data) -> None:
        #we send the data here to the database after registering The User 
        data_sent = self.registering_Data(data)
        data_sent["token"] = str(self.generate_Save_Token())
        try:
           if self.checking_Validation(data_sent["Email"])==False:
               self.my_collect.insert_one(data_sent)
               return True
           else:
                print("Acc already Exists")
                return False
        except pymongo.errors.InvalidOperation:
            print("Invalid Operation sorry ")
            return False
    #Emails sent 
    def sending_emails(self,name,email):
         client = MailerLite.Client({
          "api_key":os.environ.get("EMAIL_TOKEN")
         })
        #  print(os.environ.get("EMAIL_TOKEN"))
         url = "https://connect.mailerlite.com/"
         url2 = "https://api.mailerlite.com/api/v2/groups/121482735113995405/subscribers"
         data = {
             "name":name,
             "email": email,
         }
         payload = json.dumps(data)
         headers = {
                    "content-type": "application/json",
                    "x-mailerlite-apikey": os.environ.get("EMAIL_TOKEN")
         }
         response = requests.request("post",url2,headers=headers,data=payload)
         return response.status_code==200
    


    #Checking the presence of the email , if present don't register
    def checking_Validation(self,email):
        query = {"Email":email}
        z = self.my_collect.find_one(query)
        print(z)
        if z:
            return z,True
        else:
            return False
    
    


         
  
# if __name__ == "__main__":
#     x = Databases()
#     z = x.sending_data(["baker","lawzi","bakricoder71@gmail.com","ahmad"])
#     if z:
#        print(x.sending_emails(email="bakricoder71@gmail.com",name="bachir"))
#     else:
#         print("Not working")



        

