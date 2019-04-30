'''
Module Name:viewAllCars
Description: It displays all the list of carpool available from carpoolDetails.txt
Last edited by:Dinesh
Date:06/10/2018
'''

def viewAllCars():
    f = open('carpoolDetails.txt', 'r')                                     #opens carpoolDetails.txt
    contents = f.readlines()                                                #SAVES THE DOCUMENT LINE BY LINE in variable contents
    f.close()                                                               #close the file variable
    print('\n')
    for lines in contents:                                                  #for each line in document
        cname,dname,location,destination,ratings=lines.strip().split(',')   #retrieves carpool,drivername, location ,destination of carpool and ratings
        print(cname,location,destination)                                   #displays carname ,location and destination
