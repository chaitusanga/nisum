#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:21:26 2018

@author: nisum
"""
#import HTML
import json
import datetime
import urllib.request
import urllib
import sys

#job_id = input("Enter the Job ID ")

job_id = '5853'

user_id = ' '
user_name = ' '

def get_url():
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
    wfapi_query_string = "/wfapi"
    json_api_string = "/api/json"
    
    job_url = URL + job_id + wfapi_query_string
    
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
                desc = fields[1]
            if "userId" in line:
                user_id = fields[1]
            if "userName" in line:
                user_name = fields[1]
            
    return (desc, user_id, user_name)


#https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/5763/api/json?pretty=true


def parse_json_html():
    
    #user_id, user_name = get_url()
    desc, user_id, user_name = get_url()
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    allItems = x['stages']
    html_file_name = 'log.html'
    
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
        myFile.write('<p> <b> Build No.: </b>' + job_id + '</p>')
        myFile.write('<p> <b> UserId: </b>' + user_id + '</p>')
        myFile.write('<p> <b> User Name: </b>' + user_name + '</p>')
        
        
        myFile.write('<table style="width:100%">')
        
        
        myFile.write('<tr>')
        myFile.write('<th>Task</th>')
        myFile.write('<th>StartTime</th>')            
        myFile.write('<th>Duration</th>')
        myFile.write('<th>Status</th>')
        myFile.write('</tr>')
        
        
        for dic in allItems:

            startTime = dic['startTimeMillis'] / 1000.0
            timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S %z')
            
            duration = (dic['durationMillis'] / 1000.0)%60
            durTime = datetime.datetime.fromtimestamp(duration).strftime('%H:%M:%S')
            
#            job_status = str(dic['status'])
#            
#            if job_status == "FAILED":
#                myFile.write('<tr style="background-color:Tomato;">')
#                myFile.write('<td>' + dic['name'] + '</td>')
#                myFile.write('<td>'+ timeStamp+'</td>')            
#                myFile.write('<td>'+ durTime+'</td>')            
#                myFile.write('<td>' + dic['status'] + '</td>')
#                myFile.write('</tr>')
            
            
            
            myFile.write('<tr>')
            
            if dic['name'] == "Recycle":
                continue
            
            if dic['name'] == "Recycle Customer":
                #myFile.write('<td colspan="4">' + dic['name'] + ' --- Parallel Stage</td>')
                #continue
                myFile.write('<td>' + dic['name'] + '</td>' + '<td rowspan="3"> Recycle </td>')
            
            elif dic['name'] == "Recycle web":
                myFile.write('<td colspan="4">' + dic['name'] + ' --- Parallel Stage</td>')
                continue
            else:
                myFile.write('<td>' + dic['name'] + '</td>')
            myFile.write('<td>'+ timeStamp+'</td>')            
            myFile.write('<td>'+ durTime+'</td>')     
            
            job_status = str(dic['status'])

            if job_status == "NOT_EXECUTED":
                myFile.write('<td style="background-color:Cyan;">' + dic['status'] + '</td>')
            elif job_status == "FAILED":
                myFile.write('<td style="background-color:Red;">' + dic['status'] + '</td>')
            else:
                myFile.write('<td>' + dic['status'] + '</td>')
                
            myFile.write('</tr>')
            
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')
            

get_url()
parse_json_html()