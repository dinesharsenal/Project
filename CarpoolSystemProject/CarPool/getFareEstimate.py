'''
Module Name: getFareEstiate
Description: It provides rate to user
Last edited by:Dinesh
Date:06/10/2018
'''

import datetime
import getRates as gr
import calculateFare as calfare
def getFareEstimate():

    now = datetime.datetime.time(datetime.datetime.now())                                                       #get date timestamp
    rate=int(gr.getRates())                                                                                     #it get rates using getRates
    print('The rate at time %s:%s is %d Rs per km' %(str(now.hour).zfill(2),str(now.minute).zfill(2),rate))     #displays  rate to user
    dis=int(input('Enter distance in kms : '))                                                                  #enter ditance
    fare=calfare.calculateFare(rate,dis)                                                                        #calculates fare
    print('Total estimated fare is : %s Rs'%(str(fare)))
    return fare                                                                                                 #retuns fare
