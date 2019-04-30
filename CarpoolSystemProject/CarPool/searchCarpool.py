'''
Module Name: searchPool
Description: It gives a list of carpool to user based on input location and destination which are passed as parameters
Last edited by:Dinesh
Date:06/10/2018
'''
def searchCarpool(location,destination):
    f=open("carpoolDetails.txt","r")
    ls=[]
    count=1;
    for lines in f:
        carname,drivername,location1,destination1,rating=lines.strip().split(",")
        if destination== destination1 and location==location1:
            print(str(count)+' Car Found!')
            print('Car Name : '+carname,)
            print('Driver name: ',drivername)
            print('Driver Ratings',rating)
            s=carname+","+drivername+','+location1+","+destination1+','+rating
            ls.append(s)
            count=count+1;
    if not ls:
        print('No cars found for ' + destination + ' location :(')
    else:
        return ls
