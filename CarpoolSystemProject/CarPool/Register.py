'''
Module Name: register
Description: it gets data from user using getdata function nd creates account fo user
Last edited by:Dinesh
Date:06/10/2018
'''
import getData as gd
import GenerateAccount as ga

def register():
    username,password=gd.getData()
    ga.generateAccount(username,password)                           #using generate account function
    return True
