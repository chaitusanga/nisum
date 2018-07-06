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
#from pytz import timezone
#import pymysql
import re
import mysql.connector

#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config



#import sys

#job_id = input("Enter the Job ID ")

#job_id = '6004'

user_id = ' '
user_name = ' '
obj = []
job_number = []
jobs_info = []
resultset = []
result = []
task_result = []
tasks_info = []


import pytz

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
    
    ####Getting json api data####
    
    with urllib.request.urlopen(user_info_url) as user_url:
        user_data = json.loads(user_url.read().decode('utf-8'))
    
    with open('jenkins-jobs-info.json', 'w') as f:
        json.dump(user_data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    with open('jenkins-jobs-info.json', 'r') as info:
        obj = json.load(info)
        
        for job in obj['builds']:
            job_num = str(job['number'])
            #print(job_num)
            job_number.append(job_num)
    
            #print(job_number)
    return(job_number)


def connect_DB():


    conn = mysql.connector.connect(
         user='jenkins',
         password='nisum@123',
         host='localhost',
         database='jenkins_jobs')
    
    cur = conn.cursor()
    query = ("SELECT * FROM Build_Info")
    
    cur.execute(query)
    
    for (Env_ID, Build_ID, User_ID, User_Name, Build_URL) in cur:
        print("{}, {}, {}, {}".format(Env_ID, Build_ID, User_ID, User_Name, Build_URL))
        
    cur.close()
    conn.close()
    



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




def get_url(job_id):
    
    get_job_id = job_id
    #print(get_job_id)
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
    wfapi_query_string = "/wfapi"
    json_api_string = "/api/json"
    
    job_url = URL + get_job_id + wfapi_query_string
    
    build_url = URL + get_job_id
    
#    print(job_url)
#    print(build_url)
    
    
    ####Getting wfapi data####
    
    with urllib.request.urlopen(job_url) as url:
        data = json.loads(url.read().decode('utf-8'))
    
    with open('jenkins-log.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    user_info_url = URL + get_job_id + json_api_string
#    print(user_info_url)
    
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
            if "timestamp" in line:
                job_timestamp = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            
            
    return (job_id, build_url, desc, user_id, user_name, job_timestamp)


#https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/5763/api/json?pretty=true


def insert_db(job_ids):

    #user_id, user_name = get_url()
    job_id, build_url, desc, user_id, user_name, job_timestamp = get_url(job_ids)
    #build_url = mdb.escape_string(build_url)
    
#    print(type(build_url))
#    print(type(desc))
#    print(type(user_id))
#    print(type(user_name))
    
    
    with open('jenkins-log.json', 'r') as f:
        obj = f.read()
        x = json.loads(obj)
    
    allItems = x['stages']
    #html_file_name = 'log.html'
    

######################JOB VALIDATION ------> to be done on 07/06
    ##################VALIDATE AND PUSH TO HTML ----> TO BE DONE ON 07/06
    

    
    for dic in allItems:
        
        startTime = dic['startTimeMillis'] / 1000.0
        start_timeStamp = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S')
        start_time_convert = convert_datetime_timezone(start_timeStamp, "Asia/Kolkata", "PST8PDT")
        
        con_hour, con_min, con_sec = convertMillis(dic['durationMillis'])
        durTime = str(con_hour) + "Hrs " + str(con_min) + "Min " + str(con_sec) + "Sec"


        endTime = (dic['startTimeMillis'] + dic['durationMillis']) / 1000.0            
        end_timeStamp = datetime.datetime.fromtimestamp(endTime).strftime('%Y-%m-%d %H:%M:%S')            
        end_time_convert = convert_datetime_timezone(end_timeStamp, "Asia/Kolkata", "PST8PDT")
        
        job_time = float(job_timestamp) / 1000.0            
        job_time_date = datetime.datetime.fromtimestamp(job_time).strftime('%Y-%m-%d') 
        #print(job_time_date)
        

        ##### Insert into Build_Info table
        
        conn = mysql.connector.connect(
        user='jenkins',
        password='nisum@123',
        host='localhost',
        database='jenkins_jobs')

        
        cur = conn.cursor()
        query = """INSERT INTO Build_Info (Env_ID, Build_ID, Build_Date, User_ID, User_Name, Build_URL) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, job_time_date, user_id, user_name, build_url)
        #print(query)
        try:
            cur.execute(query)
            conn.commit()
        except:
            conn.rollback()
        
        cur.close()
        conn.close()
        
        
        
        job_status = str(dic['status'])
        
    ##### Insert into Tasks table        
    
        conn = mysql.connector.connect(
            user='jenkins',
            password='nisum@123',
            host='localhost',
            database='jenkins_jobs')
        
        
        cur = conn.cursor()
        
        try:
            
                query = """INSERT INTO Tasks (Env_ID, Build_ID, Task_Name, Start_Time, Duration, End_Time, Status) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, dic['name'], start_time_convert, durTime, end_time_convert, job_status)
                #print(query)
                cur.execute(query)
                conn.commit()

        except:
            conn.rollback()
        
        cur.close()    
        conn.close()
        
        
        
        
def get_db_build_data(jobid):
    
    
    conn1 = mysql.connector.connect(
    user='jenkins',
    password='nisum@123',
    host='localhost',
    database='jenkins_jobs')
    
    cur1 = conn1.cursor()
    

    try:
    
        cur1.execute("SELECT Env_ID, Build_ID, Build_Date, User_ID, User_Name, Build_URL FROM Build_Info WHERE Build_ID = "+ jobid)
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
        myFile.write('</tr>')
        
        for row in resultset:

            myFile.write('<tr>')
            myFile.write('<td>'+ str(row[0]) +'</td>')
            myFile.write('<td>'+ str(row[1]) +'</td>')            
            myFile.write('<td>'+ str(row[2]) +'</td>')     
            myFile.write('<td>'+ str(row[3]) +'</td>') 
            myFile.write('<td>'+ str(row[4]) +'</td>') 
            myFile.write('<td>'+ str(row[5]) +'</td>') 
            myFile.write('</tr>')
                
        myFile.write('</table>')
#        myFile.write('</body>')
#        myFile.write('</html>')              


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
        
#        myFile.write('<html>')
#        myFile.write('<head>')
#        myFile.write('<style>')
#        myFile.write('table, th, td {border: 1px solid black;}')
#        myFile.write('</style>')
#        myFile.write('</head>')
#        
#        
#        myFile.write('<body>')
#        
        myFile.write('<h2> Jenkins Job\'s Tasks Information </h2>')
#        myFile.write('<p> <b> Environment: </b>' + desc + '</p>')
#        myFile.write('<p> <b> Build No.: </b>' + job_id + '</p>')
#        myFile.write('<p> <b> UserId: </b>' + user_id + '</p>')
#        myFile.write('<p> <b> User Name: </b>' + user_name + '</p>')
        
        
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
                
#                myFile.write('<td>'+ str(row[0]) +'</td>')
#                myFile.write('<td>'+ str(row[1]) +'</td>')
                
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
                myFile.write('<td>' + str(row[3]) + " PST" + '</td>')            
                myFile.write('<td>' + str(row[4]) + '</td>')     
                myFile.write('<td>' + str(row[5]) + " PST" + '</td>') 
                
                job_status = str(row[6])
    
                if job_status == "NOT_EXECUTED":
                    myFile.write('<td style="background-color:Cyan;">' + str(row[6]) + '</td>')
                    myFile.write('</tr>')
                    flag = 0
                elif job_status == "FAILED" and str(row[2]) == "Recycle Order":
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
                
                myFile.write('<td>' + str(row[3]) + " PST" + '</td>')            
                myFile.write('<td>' + str(row[4]) + '</td>')     
                myFile.write('<td>' + str(row[5]) + " PST" + '</td>') 
                myFile.write('<td>'+ " " +'</td>')
                
                myFile.write('</tr>')
                
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')



#jobs_list = job_ids_list()
#print(jobs_list)

#jobs_list = ['6470', '6469', '6468', '6467', '6466', '6465', '6464', '6463', '6462', '6461', '6460', '6459', '6458', '6457', '6456', '6455', '6454', '6453', '6452', '6451', '6450', '6449', '6448', '6447', '6446', '6445', '6444', '6443', '6442', '6441', '6440', '6439', '6438', '6437', '6436', '6435', '6434', '6433', '6432', '6431', '6430', '6429', '6428', '6427', '6426', '6425', '6424', '6423', '6422', '6421', '6420', '6419', '6418', '6417', '6416', '6415', '6414', '6413', '6412', '6411', '6410', '6409', '6408', '6407', '6406', '6405', '6404', '6403', '6402', '6401', '6400', '6399', '6398', '6397', '6396', '6395', '6394', '6393', '6392', '6391', '6390', '6389', '6388', '6387', '6386', '6385', '6384', '6383', '6382', '6381', '6380', '6379', '6378', '6377', '6376', '6375', '6374', '6373', '6372', '6371']


#job_ids_list()
#for ids in jobs_list:
#    #get_url(ids)
#    #insert_db(ids)
#    jobs_info = get_db_data(ids)
#    

job_id = input("Enter the Job ID ")

job_info = get_db_build_data(job_id)
display_db_build_data(job_info)

tasks_info = get_db_task_data(job_id)
display_db_task_data(tasks_info)
#print(tasks_info)

#    for row in jobs_info:
#        print(row[0], row[1], row[2], row[3], row[4], row[5])





#get_url()
#insert_db()
#connect_DB()