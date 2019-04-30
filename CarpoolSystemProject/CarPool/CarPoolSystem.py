'''
Module Name: carPoolSystem
Description: It gives multiple options to user to ceate account,login,enter carpool system,or view ratings of different drivers
Last edited by:Dinesh
Date:06/10/2018
'''

import Register as rg
import Login as lg
import carPool as cc
import viewRating as vr

def carpoolSystem():
    while True:
        print("\nEnter your choice\n1.Register\n2.Login\n3.Carpool\n4.View Ratings\n5.Quit")
        choice = int(input())
        if choice == 1:                 #Register a new account
            rg.register()
        elif choice == 2:               #Login into account
            lg.login()
        elif choice==3:                 #Get into carpool and view different carpool options
            cc.carpool()
        elif choice==4:                 #View rating of different carpool
            vr.viewRating()   # ga
        elif choice==5:              ##################   #Exit
            break


carpoolSystem()
