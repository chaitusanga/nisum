#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:07:49 2018

@author: nisum
"""

obj={}
fields = []

import json
import datetime
#import sys
import csv
#import math



def convertMillis(millis):
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000*60) ) % 60
    minutes = int(minutes)
    hours = (millis / (1000*60*60)) % 24
    hours = int(hours)

    return(hours, minutes, seconds)
    

#x = convertMillis(19135435)
#print(x)


def main():
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    
    allItems = x['stages']
    
    with open('data.csv', 'w', newline='') as newCSV:
        fieldnames = ['Task', 'StartTime', 'Duration', 'Status']
        
        csvWriter = csv.writer(newCSV)
        csvWriter.writerow(fieldnames)
    
        for dic in allItems:
            fields = []
            startTime = dic['startTimeMillis'] / 1000.0
            timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S %z')
            
            con_hour, con_min, con_sec = convertMillis(dic['durationMillis'])
            
            print(con_hour, con_min, con_sec)
            
            durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"
            
            #durTime = print("{0}:{1}:{2}".format(con_hour, con_min, con_sec))
#            print(type(convert_mill(dic['durationMillis'])))
#            durTime = convert_mill(dic['durationMillis'])
            
            #durTime = duration + "Sec"
            #duration = (dic['durationMillis'])
            #durTime = datetime.datetime.fromtimestamp(duration).strftime('%H:%M:%S')
            #durTime = convertMillis(int(dic['durationMillis']))
            #print(dic['name'] + "," + timeStamp + "," + durTime + "," + dic['status'])
        
            #fields = dic['name'] + "," + timeStamp + "," + durTime + "," + dic['status']
            #fields = dic['name'] + timeStamp + durTime + dic['status']
            #fields = [dic['name'] + "--" + timeStamp + "--" + durTime + "--" + dic['status'] ]
            
            #fields.append(dic['name'] + "," + timeStamp + "IST," + str(duration) + "," + dic['status'] )
            #abc = len(fields)
            fields.append(dic['name'] + "," + timeStamp + "IST," + durTime + "," + dic['status'] )
            #print(abc)
            #print(fields)
            csvWriter.writerow(fields)
            
    #        
    #        for i in fields:
    #            csvWriter.writerow(i)
    
                startTime = dic['startTimeMillis'] / 1000.0
            timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S %z')
            
            con_hour, con_min, con_sec = convertMillis(dic['durationMillis'])
            durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"
            
main()