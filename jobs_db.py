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
from pytz import timezone
import pymysql
import re
import mysql.connector

#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config



#import sys

job_id = input("Enter the Job ID ")

#job_id = '6004'

user_id = ' '
user_name = ' '


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
            job_number = str(job['number'])
            
    return(job_number)


def connect_DB():
#    # Open database connection
#    db = pymysql.connect("localhost","jenkins","nisum@123","jenkins_jobs" )
#    
#    # prepare a cursor object using cursor() method
#    cursor = db.cursor()
#    
#    # execute SQL query using execute() method.
#    #cursor.execute("SHOW TABLES")
#    
#    sql = """DESC Build_Info"""
#    
#    
#    # Fetch a single row using fetchone() method.
#    cursor.execute(sql)
#    results = cursor.fetchall()
#    print(results)
#    
#    #print ("Tables List " % data)
#    
#    # disconnect from server
#    db.close()
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
            if "timestamp" in line:
                job_timestamp = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            
            
    return (build_url, desc, user_id, user_name, job_timestamp)


#https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/5763/api/json?pretty=true


def insert_db():

    #user_id, user_name = get_url()
    build_url, desc, user_id, user_name, job_timestamp = get_url()
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
    
    conn = mysql.connector.connect(
            user='jenkins',
            password='nisum@123',
            host='localhost',
            database='jenkins_jobs')
    
    
    ##### Insert into Build_Info table
    
    cur = conn.cursor()
    query = """INSERT INTO Build_Info (Env_ID, Build_ID, User_ID, User_Name, Build_URL) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, user_id, user_name, build_url)
    #print(query)
    try:
        cur.execute(query)
        conn.commit()
    except:
        conn.rollback()
    
    conn.close()
    
    ##### Insert into Build_Info table
    
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
        
        
        job_status = str(dic['status'])
        
        
        conn = mysql.connector.connect(
            user='jenkins',
            password='nisum@123',
            host='localhost',
            database='jenkins_jobs')
        
        
        cur = conn.cursor()
        
        try:
            
            #job_val_query = """SELECT count(*) FROM Tasks WHERE Val1 = '%s' AND Val2 = '%s'""" % (Env_ID, Task_Name)
 
#            cur.execute("SELECT COUNT(*) FROM Tasks WHERE Env_ID = '%s' AND Task_Name = '%s'" % (desc, dic['name']))
#            print(job_query_status)
#            job_query_result=cur.fetchone()
#            job_result = job_query_result[0]
            
            #print(job_result)
    
#            if job_result == 0:
                query = """INSERT INTO Tasks (Env_ID, Build_ID, Task_Name, Start_Time, Duration, End_Time, Status) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");""" % (desc, job_id, dic['name'], start_time_convert, durTime, end_time_convert, job_status)
                #print(query)
                cur.execute(query)
                conn.commit()

        except:
            conn.rollback()
        
        
    conn.close()
        


jobs_list = job_ids_list()
for ids in jobs_list:
    get_url(ids)
#get_url()
insert_db()
#connect_DB()