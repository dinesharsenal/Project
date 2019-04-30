'''
Module Name: deleteCarpool
Description: It delete a carpool using a carpool name given by user
Last edited by:Samkit Barbhaya
Date:06/10/2018
'''

def deletecarpool(carName):
    f=open("carpoolDetails.txt","r")
    carpoolDetails=f.readlines()
    f.close()
    isDeleted=False
    for carpool in carpoolDetails:
        carname1,drivenme,location,destination,ratings=carpool.strip().split(',')
        if carName==carname1:
            carpoolDetails.remove(carName+','+drivenme+','+location+','+destination+','+ratings+'\n')
            isDeleted=True
    f=open("carpoolDetails.txt","w+")
    f.writelines(carpoolDetails)
    f.close()
    return isDeleted
