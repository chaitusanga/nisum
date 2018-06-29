#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:52:46 2018

@author: Chaitanya Sanga
"""

import json
import datetime
import csv
import urllib.request
import urllib
import pytz
import re

job_id = input("Enter the Job ID ")


def convert_datetime_timezone(dt, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)

    dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)
    dt = dt.strftime("%Y-%m-%d %H:%M:%S")

    return dt 

########### End of convert_datetime_timezone() ###########


def convertMillis(millis):
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000*60) ) % 60
    minutes = int(minutes)
    hours = (millis / (1000*60*60)) % 24
    hours = int(hours)

    return(hours, minutes, seconds)

########### End of convertMillis() ###########


def get_url():
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
    wfapi_query_string = "/wfapi"
    json_api_string = "/api/json"
    
    job_url = URL + job_id + wfapi_query_string
    
    build_url = URL + job_id
    
    ####Getting wfapi data####
    
    with urllib.request.urlopen(job_url) as url:
        data = json.loads(url.read().decode('utf-8'))
    
    with open('jenkins-log.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    user_info_url = URL + job_id + json_api_string
    
    ####Getting json api data####
    
    with urllib.request.urlopen(user_info_url) as user_url:
        user_data = json.loads(user_url.read().decode('utf-8'))
    
    with open('user_log-info.json', 'w') as f:
        json.dump(user_data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    with open('user_log-info.json', 'r') as info:
        for line in info:
            fields = line.strip().split(':')
            if "description" in line:
                desc = re.sub('[^A-Za-z0-9-]+', '', fields[1])
            if "userId" in line:
                user_id = re.sub('[^A-Za-z0-9-]+', '', fields[1])
            if "userName" in line:
                user_name = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            
    return (build_url, desc, user_id, user_name)
    
    

########### End of get_url() ###########


def parse_json_html():
    
    flag = 0
    
    build_url, desc, user_id, user_name = get_url()
    
    build_url_html = '<a href="' + build_url + '">' + build_url + '</a>'
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    allItems = x['stages']
    html_file_name = job_id + '.html'
    
    with open(html_file_name, 'w') as myFile:
        
        myFile.write('<html>')
        myFile.write('<head>')
        myFile.write('<style>')
        myFile.write('table, th, td {border: 1px solid black;}')
        myFile.write('</style>')
        myFile.write('</head>')
        
        
        myFile.write('<body>')
        
        myFile.write('<h2> Jenkins Job Information </h2>')
        myFile.write('<p> <b> Environment: </b>' + desc + '</p>')
        myFile.write('<p> <b> Build URL: </b>' + build_url_html + '</p>')
        myFile.write('<p> <b> Build No.: </b>' + job_id + '</p>')
        myFile.write('<p> <b> UserId: </b>' + user_id + '</p>')
        myFile.write('<p> <b> User Name: </b>' + user_name + '</p>')
        
        
        myFile.write('<table style="width:100%">')
    
    
        myFile.write('<tr>')
        myFile.write('<th colspan="2">Task</th>')
        myFile.write('<th>Start Time</th>')            
        myFile.write('<th>Duration</th>')
        myFile.write('<th>End Time</th>')
        myFile.write('<th>Status</th>')
        myFile.write('</tr>')
        
        for dic in allItems:



            startTime = dic['startTimeMillis'] / 1000.0
            start_timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S')
            start_time_convert = convert_datetime_timezone(start_timeStamp, "Asia/Kolkata", "PST8PDT")
            
            con_hour, con_min, con_sec = convertMillis(dic['durationMillis'])
            durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"


            endTime = (dic['startTimeMillis'] + dic['durationMillis']) / 1000.0            
            end_timeStamp = datetime.datetime.fromtimestamp(endTime).strftime('%Y-%m-%d %H:%M:%S')            
            end_time_convert = convert_datetime_timezone(end_timeStamp, "Asia/Kolkata", "PST8PDT")


            if flag == 0:
                
                myFile.write('<tr>')
                
                if dic['name'] == "Recycle":
                    myFile.write('<td rowspan="4">' + dic['name'] + '</td>')
                    continue
                
                if dic['name'] == "Recycle web":
                    myFile.write('<td rowspan="3">' + dic['name'] + '</td>')
                    continue
                
                if dic['name'] == "Recycle Customer" or dic['name'] == "Recycle Order" or dic['name'] == "Recycle Promotion":
                    myFile.write('<td>' + dic['name'] + '</td>')
                    
                elif dic['name'] == "Recycle WSSG" or dic['name'] == "Recycle NavApp":
                    myFile.write('<td>' + dic['name'] + '</td>')
                    
                else:
                    myFile.write('<td colspan="2">' + dic['name'] + '</td>')
                myFile.write('<td>'+ start_time_convert + " PST" +'</td>')            
                myFile.write('<td>'+ durTime+'</td>')     
                myFile.write('<td>'+ end_time_convert + " PST" +'</td>') 
                
                job_status = str(dic['status'])
    
                if job_status == "NOT_EXECUTED":
                    myFile.write('<td style="background-color:Cyan;">' + dic['status'] + '</td>')
                    myFile.write('</tr>')
                    flag = 0
                elif job_status == "FAILED":
                    myFile.write('<td style="background-color:Red;">' + dic['status'] + '</td>')
                    myFile.write('</tr>')
                    flag = 1
                else:
                    myFile.write('<td>' + dic['status'] + '</td>')
                    myFile.write('</tr>')                
                
            else:
                 
                myFile.write('<tr>')
                
                if dic['name'] == "Recycle":
                    myFile.write('<td rowspan="4">' + dic['name'] + '</td>')
                    continue
                
                if dic['name'] == "Recycle web":
                    myFile.write('<td rowspan="3">' + dic['name'] + '</td>')
                    continue
                
                if dic['name'] == "Recycle Customer" or dic['name'] == "Recycle Order" or dic['name'] == "Recycle Promotion":
                    myFile.write('<td>' + dic['name'] + '</td>')
                    
                elif dic['name'] == "Recycle WSSG" or dic['name'] == "Recycle NavApp":
                    myFile.write('<td>' + dic['name'] + '</td>')
                    
                else:
                    myFile.write('<td colspan="2">' + dic['name'] + '</td>')
                
                myFile.write('<td>'+ start_time_convert + " PST" +'</td>')            
                myFile.write('<td>'+ durTime+'</td>')   
                myFile.write('<td>'+ end_time_convert + " PST" +'</td>') 
                myFile.write('<td>'+ " " +'</td>')
                
                myFile.write('</tr>')
                
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')              
                
            
######### End of parse_json_html()#########
        
        

def parse_json():
    
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
            durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"
            
            
            fields.append(dic['name'] + "," + timeStamp + "IST," + durTime + "," + dic['status'])
            csvWriter.writerow(fields)

######### End of parse_json()#########


get_url()
#parse_json()
parse_json_html()