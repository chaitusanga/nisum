#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:21:26 2018

@author: Chaitanya Sanga
"""

import json
import datetime
import urllib.request
import urllib
import re
import mysql.connector
import pytz



user_id = ' '
user_name = ' '
dic = []
obj = []
job_number = []
jobs_info = []
resultset = []
result = []
task_result = []
tasks_info = []


def convert_datetime_timezone(dt, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)

    dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)
    dt = dt.strftime("%Y-%m-%d %H:%M:%S")

    return dt 


def job_ids_list():
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles"
    
    json_api_string = "/api/json"
    
    user_info_url = URL + json_api_string
    
    with urllib.request.urlopen(user_info_url) as user_url:
        user_data = json.loads(user_url.read().decode('utf-8'))
    
    with open('jenkins-jobs-info.json', 'w') as f:
        json.dump(user_data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    with open('jenkins-jobs-info.json', 'r') as info:
        obj = json.load(info)
        
        for job in obj['builds']:
            job_num = str(job['number'])
            job_number.append(job_num)
            
    return(job_number)


def convertMillis(millis):
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000*60) ) % 60
    minutes = int(minutes)
    hours = (millis / (1000*60*60)) % 24
    hours = int(hours)

    return(hours, minutes, seconds)


def get_url(job_id):
    
    get_job_id = job_id
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
    wfapi_query_string = "/wfapi"
    json_api_string = "/api/json"
    
    job_url = URL + get_job_id + wfapi_query_string
    
    build_url = URL + get_job_id
    
    with urllib.request.urlopen(job_url) as url:
        data = json.loads(url.read().decode('utf-8'))
    
    with open('jenkins-log.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    user_info_url = URL + get_job_id + json_api_string

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
            if "timestamp" in line:
                job_timestamp = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            if "result" in line:
                status = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            
            
    return (job_id, build_url, desc, user_id, user_name, job_timestamp, status)


def insert_db(job_ids):

    job_id, build_url, desc, user_id, user_name, job_timestamp, status = get_url(job_ids)
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    allItems = x['stages']
   

    conn = mysql.connector.connect(
    user='jenkins',
    password='nisum@123',
    host='localhost',
    database='jenkins_jobs')

    job_time = float(job_timestamp) / 1000.0            
    job_time_date = datetime.datetime.fromtimestamp(job_time).strftime('%Y-%m-%d') 

    cur = conn.cursor()
    cur.execute("SELECT COUNT(Build_ID) FROM Build_Info WHERE Build_ID = "+ job_id)
    job_exist = cur.fetchone()


    if job_exist[0] == 0:
        
        cur1 = conn.cursor()
        
        try:
            
            query = """INSERT INTO Build_Info (Env_ID, Build_ID, Build_Date, User_ID, User_Name, Build_URL, Status) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, job_time_date, user_id, user_name, build_url, status)
            cur1.execute(query)
            conn.commit()
            
        except:
            
            conn.rollback()

        cur1.close()

    
    for dic in allItems:
        
        startTime = dic['startTimeMillis'] / 1000.0
        start_timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S')
        start_time_convert = convert_datetime_timezone(start_timeStamp, "Asia/Kolkata", "PST8PDT")
        #start_time_convert = start_time_convert + "PST"
        
        con_hour, con_min, con_sec = convertMillis(dic['durationMillis'])
        durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"


        endTime = (dic['startTimeMillis'] + dic['durationMillis']) / 1000.0            
        end_timeStamp = datetime.datetime.fromtimestamp(endTime).strftime('%Y-%m-%d %H:%M:%S')            
        end_time_convert = convert_datetime_timezone(end_timeStamp, "Asia/Kolkata", "PST8PDT")
        end_time_convert = end_time_convert + "PST"
        
        
        conn = mysql.connector.connect(
        user='jenkins',
        password='nisum@123',
        host='localhost',
        database='jenkins_jobs')

            
        job_status = str(dic['status'])
        
        cur2 = conn.cursor()

        try:
    
            query = """INSERT INTO Tasks (Env_ID, Build_ID, Task_Name, Start_Time, Duration, End_Time, Status) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, dic['name'], start_time_convert, durTime, end_time_convert, job_status)
            cur2.execute(query)
            conn.commit()
            
        except:
            
            conn.rollback()

        cur2.close()  

        conn.close()


def get_db_build_data(jobid):
    
    
    conn1 = mysql.connector.connect(
    user='jenkins',
    password='nisum@123',
    host='localhost',
    database='jenkins_jobs')
    
    cur1 = conn1.cursor()
    

    try:
    
        cur1.execute("SELECT Env_ID, Build_ID, Build_Date, User_ID, User_Name, Build_URL, Status FROM Build_Info WHERE Build_ID = "+ jobid)
        result = cur1.fetchall()
            
    except:
        
        print("Job ID "+ jobid + "not selected")
       
        
    cur1.close()
    conn1.close()

    return(result)


def display_db_build_data(jobs_info):
    
    resultset = jobs_info
    html_file_name = 'build_info.html'
    
    with open(html_file_name, 'w') as myFile:
        
        myFile.write('<html>')
        myFile.write('<head>')
        myFile.write('<style>')
        myFile.write('table, th, td {border: 1px solid black;}')
        myFile.write('</style>')
        myFile.write('</head>')
        
        
        myFile.write('<body>')
        
        myFile.write('<h2> Jenkins Job Information </h2>')

        myFile.write('<table style="width:100%">')
        
        myFile.write('<tr>')
        myFile.write('<th>Env ID</th>')
        myFile.write('<th>Job ID</th>')            
        myFile.write('<th>Date</th>')
        myFile.write('<th>User ID</th>')
        myFile.write('<th>User Name</th>')
        myFile.write('<th>URL</th>')
        myFile.write('<th>Status</th>')
        myFile.write('</tr>')
        
        for row in resultset:

            myFile.write('<tr>')
            myFile.write('<td>'+ str(row[0]) +'</td>')
            myFile.write('<td>'+ str(row[1]) +'</td>')            
            myFile.write('<td>'+ str(row[2]) +'</td>')     
            myFile.write('<td>'+ str(row[3]) +'</td>') 
            myFile.write('<td>'+ str(row[4]) +'</td>') 
            myFile.write('<td>'+ str(row[5]) +'</td>') 
            myFile.write('<td>'+ str(row[6]) +'</td>') 
            myFile.write('</tr>')
                
        myFile.write('</table>')


def get_db_task_data(jobid):
    
    conn1 = mysql.connector.connect(
    user='jenkins',
    password='nisum@123',
    host='localhost',
    database='jenkins_jobs')
    
    cur1 = conn1.cursor()
    

    try:
    
        cur1.execute("SELECT Env_ID, Build_ID, Task_Name, Start_Time, Duration, End_Time, Status FROM Tasks WHERE Build_ID = "+ jobid)
        task_result = cur1.fetchall()
        
    except:
        print("Job ID" + jobid + "not found")

    cur1.close()
    conn1.close()

    return(task_result)


def display_db_task_data(tasks_info):
    
    task_resultset = tasks_info
    
    flag = 0
    html_file_name = 'build_info.html'
    
    with open(html_file_name, 'a') as myFile:
        
        myFile.write('<h2> Jenkins Job\'s Tasks Information </h2>')

        myFile.write('<table style="width:100%">')
        
        myFile.write('<tr>')
        myFile.write('<th colspan="2">Task</th>')
        myFile.write('<th>Start Time</th>')            
        myFile.write('<th>Duration</th>')
        myFile.write('<th>End Time</th>')
        myFile.write('<th>Status</th>')
        myFile.write('</tr>')
        
        
        for row in task_resultset:
                
            if flag == 0:                
                
                myFile.write('<tr>')
                
                if str(row[2]) == "Recycle":
                    myFile.write('<td rowspan="4">' + str(row[2]) + '</td>')
                    continue
                
                if str(row[2]) == "Recycle web":
                    myFile.write('<td rowspan="3">' + str(row[2]) + '</td>')
                    continue
                
                if str(row[2]) == "Recycle Customer" or str(row[2]) == "Recycle Order" or str(row[2]) == "Recycle Promotion":
                    myFile.write('<td>' + str(row[2]) + '</td>')
                    
                elif str(row[2]) == "Recycle WSSG" or str(row[2]) == "Recycle NavApp":
                    myFile.write('<td>' + str(row[2]) + '</td>')
                    
                else:
                    myFile.write('<td colspan="2">' + str(row[2]) + '</td>')
                myFile.write('<td>' + str(row[3]) + '</td>')            
                myFile.write('<td>' + str(row[4]) + '</td>')     
                myFile.write('<td>' + str(row[5]) + '</td>') 
                
                job_status = str(row[6])
    
                if job_status == "NOT_EXECUTED":
                    myFile.write('<td style="background-color:Cyan;">' + str(row[6]) + '</td>')
                    myFile.write('</tr>')
                    flag = 0
                elif job_status == "IN_PROGRESS":
                    myFile.write('<td style="background-color:Yellow;">' + str(row[6]) + '</td>')
                    myFile.write('</tr>')
                    flag = 0
                elif job_status == "FAILED":
                    myFile.write('<td style="background-color:Red;">' + str(row[6]) + '</td>')
                    myFile.write('</tr>')
                    flag = 1
                else:
                    myFile.write('<td>' + str(row[6]) + '</td>')
                    myFile.write('</tr>')

            else:
                myFile.write('<tr>')
                
                if str(row[2]) == "Recycle":
                    myFile.write('<td rowspan="4">' + str(row[2]) + '</td>')
                    continue
                
                if str(row[2]) == "Recycle web":
                    myFile.write('<td rowspan="3">' + str(row[2]) + '</td>')
                    continue
                
                if str(row[2]) == "Recycle Customer" or str(row[2]) == "Recycle Order" or str(row[2]) == "Recycle Promotion":
                    myFile.write('<td>' + str(row[2]) + '</td>')
                    
                elif str(row[2]) == "Recycle WSSG" or str(row[2]) == "Recycle NavApp":
                    myFile.write('<td>' + str(row[2]) + '</td>')
                    
                else:
                    myFile.write('<td colspan="2">' + str(row[2]) + '</td>')
                
                myFile.write('<td>' + str(row[3]) + '</td>')            
                myFile.write('<td>' + str(row[4]) + '</td>')     
                myFile.write('<td>' + str(row[5]) + '</td>') 
                myFile.write('<td>'+ " " +'</td>')
                
                myFile.write('</tr>')
                
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')



#############Main

jobs_list = job_ids_list()

jobs_list_sort = sorted(jobs_list)
        
#for ids in jobs_list_sort:
#    insert_db(ids)

job_id = input("Enter the Job ID ")

job_info = get_db_build_data(job_id)
display_db_build_data(job_info)

tasks_info = get_db_task_data(job_id)
display_db_task_data(tasks_info)


