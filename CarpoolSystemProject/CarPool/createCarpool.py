'''
Module Name: createCarpool
Description: It takes input of carpool details using carpool data parameter and puts it into the carpoolDetails.txt file
Last edited by:Samkit Barbhaya
Date:06/10/2018
'''

def createCarpool(carpoolData):
    f=open("carpoolDetails.txt","a+")
    f.write(carpoolData+'\n')
    f.close()

