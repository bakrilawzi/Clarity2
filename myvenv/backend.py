import pymongo
import sys
import hashlib
import os
import json 
import pymongo.errors
from secrets import token_bytes
import time
from oauthlib.oauth2 import WebApplicationClient 
import smtplib
from email.message import EmailMessage
from authentications import authenticates

#send the data and authenticate
class backend:
    
    def __init__(self,databaseName,databseCollect):
        pass
    







x = backend("Clarity","Users")
data = ["baker","lawzi","bakricoder71@gmail.com","123"]
x.sending_data(data)











# pasword = "Arsindanslombredelupin12"
# salt = os.urandom(32)
# hashed_pass = hashlib.pbkdf2_hmac("sha256",pasword.encode("utf-8"),salt,100000)

