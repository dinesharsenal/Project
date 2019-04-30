'''
Module Name: GenerateAccount
Description: It accepts username,password from user using parameters and saves the acount in UserData.txt file
Last edited by:Samkit Barbhaya
Date:06/10/2018
'''

import time
def generateAccount(username,password):
    print("Creating account...")
    text_file = open("UserData.txt", "a+")                      #opens userdata.txt in vaiable
    text_file.write(username + ":" + password + '\n')           #writes into file uername,password
    time.sleep(1)
    print("Account has been created")
