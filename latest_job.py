#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:30:43 2018

@author: nisum
"""

import json
import datetime
import urllib.request
import urllib



def get_url():
    
    URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
    #wfapi_query_string = "/wfapi"
    json_api_string = "lastBuild/api/json"
    
    job_url = URL + json_api_string
    
    ####Getting wfapi data####
    
    with urllib.request.urlopen(job_url) as url:
        data = json.loads(url.read().decode('utf-8'))
    
    with open('latest-job-log.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)
        f.write('\n')
    
    #user_info_url = URL + job_id + json_api_string
    
    ####Getting json api data####
    
#    with urllib.request.urlopen(user_info_url) as user_url:
#        user_data = json.loads(user_url.read().decode('utf-8'))
#    
#    with open('user_log-info.json', 'w') as f:
#        json.dump(user_data, f, indent=4, separators=(',', ': '), sort_keys=True)
#        f.write('\n')
    
    with open('latest-job-log.json', 'r') as info:
        for line in info:
            fields = line.strip().split(':')
            if "description" in line:
                desc = fields[1]
            if "id" in line:
                user_id = fields[1]
#            if "userName" in line:
#                user_name = fields[1]
            
    return (desc, user_id)



get_url()