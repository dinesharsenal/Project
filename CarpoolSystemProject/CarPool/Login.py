import verifyPassword as vp
import getData as gd

'''
Module Name: Login
Description: It takes username,password as parameters and returns true if credentials match with those in UserData text file,else prints invalid data
Last edited by:Dinesh
Date:06/10/2018
'''

#login
def login():
    username, password = gd.getData()                   #get username,password from getData function module
    if vp.verifyPassword(username, password):           #verifies password
        print('Successfully Logged in')
        return True
    else:
        print("Invalid username or password")
