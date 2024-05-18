import hashlib
import os
from secrets import token_bytes
import time

class mangementPass:
    def __init__(self):
        pass
    #Encrypting The password to enhance Security
    def salt_Password(self,password) -> str:
        salt = os.urandom(32)
        hashed_pass = hashlib.pbkdf2_hmac("sha256",password.encode("utf-8"),salt,100000)
        return salt,hashed_pass
    
    #Generating tokens for secure communications between the user and database
    def generate_Save_Token(self) -> bytes:
         #we will save the encrypted token inside the File and locked 
         #TODO changing the Logic is a mandatory
          token_generated = token_bytes(20) 
          os.makedirs("Tokens",exist_ok=True)
          file_path = os.path.join("Tokens","token.txt")
          with open(file_path,"w") as file:
              file.write(str(token_generated))
          return token_generated
    

    #Generate Time equal to 60 min for deleting the token and updating the field , making the security better
    def Token_time(self)->int:
        times  = int(time.time()) + (60*60)
        return times
    
    def verify_password(self,stored_salt, stored_hash, provided_password):
           iterations = 100000  # Must be the same as when the password was created
           hash = hashlib.pbkdf2_hmac("sha256", provided_password.encode("utf-8"), stored_salt, iterations)
           print(hash,stored_salt)
           return hash == stored_hash
    
    