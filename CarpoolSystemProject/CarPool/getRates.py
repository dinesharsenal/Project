'''
Module Name: getRates
Description: It provides rate to user for a given timestamp
Last edited by:Dinesh
Date:06/10/2018
'''
import datetime
def getRates():
    f = open('carpoolrates.txt', 'r')
    for lines in f:
        regular, afterNoonPeakCharges, midnNightPeakCharges = lines.strip().split(',')

    now = datetime.datetime.time(datetime.datetime.now())
    noon = now.replace(hour=11, minute=59, second=59, microsecond=0)
    midnight = now.replace(hour=23, minute=59, second=59, microsecond=0)
    earlymorning = now.replace(hour=5, minute=59, second=59, microsecond=0)

    if now > noon and now < midnight:
        rate = afterNoonPeakCharges
    elif now > midnight and now < earlymorning:
        rate = midnNightPeakCharges
    else:
        rate = regular

    return rate
