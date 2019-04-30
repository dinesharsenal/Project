'''
Module Name: carPool
Description: It gives all the function to the user and user can select the respective function which he wants
Last edited by:Dinesh
Date:06/10/2018
'''

import createCarpool as cc
import joinCarpool as jc
import searchCarpool as sc
import deleteCarpool as dc
import getFareEstimate as gfe
import viewAllCars as vac
def carpool():
    while True:
        print("\nEnter your choice\n1.Add Carpool\n2.Join Carpool\n3.Search Carpool\n4.Delete Carpool\n5.Get Fare Estimate\n6.View all cars\n7.Exit")
        choice = int(input())
        if choice == 1:                                                                         #add carpool
            carname = str(input("Enter carpool Name: "))
            drivername=str(input('Enter Driver name: '))
            clocation = str(input("Enter Location: "))
            cdestination = str(input("Enter Destination: "))
            defaultratings='Newly Joined'
            carpoolDetails = carname + "," +drivername+','+clocation + "," + cdestination+','+defaultratings
            cc.createCarpool(carpoolDetails)
        elif choice == 2:                                                                       #join carpool
            print('Enter Location')
            clocation = str(input())
            print('Enter Destination')
            cdestination = str(input())
            jc.joinCarpool(clocation,cdestination)

        elif choice == 3:                                                                       #search carpool
            print('Enter Location')
            clocation = str(input())
            print('Enter Destination')
            cdestination = str(input())
            sc.searchCarpool(clocation,cdestination)

        elif choice==4:                                                                         #delete carpool
            print('Enter Carpool Name to be deleted : ')
            cname=str(input())
            f=dc.deletecarpool(cname)
            if f:
                print('Deleted!')
            else:
                print('Enter proper carpool name')
        elif choice==5:                                                                         #get estimate fare for ride
            gfe.getFareEstimate()
            break
        elif choice ==6:                                                                        #view all carspool list
            vac.viewAllCars()
            break
        else:
            break
