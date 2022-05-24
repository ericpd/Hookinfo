#author : Sayyed Viquar ahmed 
import requests
import urllib
import time


def instagram(username):
    try:
        url="http://instagram.com/"+username
        print("Username found in  Instagram")
        
    except Exception  as e :
            print("Can't find the Username ")
            

def pinrest(username):
    try:
        url="http://pinrest.com/"+username
        print("Username found in Pinrest platform")
        
    except Exception as e:
        print("cant find the username")

def facebook(username):
    try:
        url="http://facebook.com/"+username
        print("Username found in FaceBook platform")
        
    except Exception as e:
        print("cant find the username")
    





        







