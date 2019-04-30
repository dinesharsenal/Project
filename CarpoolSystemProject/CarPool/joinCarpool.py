'''
Module Name:joinCarpool
Description: It displays all the list of carpool available for the given source and destination and the user selects the caarpool which he requires
Last edited by:Dinesh
Date:06/10/2018
'''

import searchCarpool as sc
import deleteCarpool as dc

def joinCarpool(location,destination):
    isSelected=False                                            #selected flag
    l=sc.searchCarpool(location,destination)                    #search carpool for given location and destination and assigns it into list
    if l:
        while(isSelected==False):                               #if not selected select any carpool using input number
            i=int(input('Select any carpool : '))
            if i>len(l) :
                print('Enter valid number!')
            else:
                print('Selected carpool is : '+l[i-1])
                isSelected=True
                a,b,c,d,e=str(l[i-1]).split(",")
                dc.deletecarpool(a)                             #delete the selected carpool so that other users cannot book
