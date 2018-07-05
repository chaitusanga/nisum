#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:46:01 2018

@author: nisum
"""

obj = []
task_name = []
name = {}

import json
#import datetime
import urllib.request
import urllib

def get_url():
    
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
            
            print(job_number)
            
            #fields = line.strip().split(':')
#            if "description" in line:
#                desc = re.sub('[^A-Za-z0-9-]+', '', fields[1])
#            if "userId" in line:
#                user_id = re.sub('[^A-Za-z0-9-]+', '', fields[1])
#            if "userName" in line:
#                user_name = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
#            if "timestamp" in line:
#                job_timestamp = re.sub('[^A-Za-z0-9 ]+', '', fields[1])
            
    
            
#    return (build_url, desc, user_id, user_name, job_timestamp)



get_url()
