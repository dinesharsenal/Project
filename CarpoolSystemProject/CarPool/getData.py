'''
Module Name:getData
Description: It takes username,password as input from user and returns them to the Login module
Last edited by:Dinesh
Date:06/10/2018
'''

def getData():
    while True:
        print("Enter username")
        username = input()                              #takes input username from user
        if not len(username) > 0:                       #if username is blank continue until valid username is input
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        print("Enter password")                         #enter password from user
        password = input()
        if not len(password) > 0:                       #password length should be greater than 0
            print("Password can't be blank")
            continue#dinesh1998.2010@gmail.com
        else:
            break
    return username,password                            #returns username,password to Login module








