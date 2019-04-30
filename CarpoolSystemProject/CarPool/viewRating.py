'''
Module Name: viewRating
Description: It
Last edited by:Dinesh
Date:06/10/2018
'''
def viewRating():
    f=open('carpoolDetails.txt','r')
    for lines in f:
        cname,name,s,d,ratings=lines.strip().split(',')
        print(cname,name,ratings)
