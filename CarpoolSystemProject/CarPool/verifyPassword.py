'''
Module Name: verifyPassword
Description: It checks whether username and password given by user matches and searches through the UserData.txt file
Last edited by:Dinesh
Date:06/10/2018
'''
# Login authorization
def verifyPassword(s_username, s_password):
    logged_in=False
    with open('UserData.txt','r') as file:
        for line in file:
            username,password=line.strip().split(":")
            if(username==s_username):
                logged_in=(password==s_password)
                break
        return logged_in
