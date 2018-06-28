#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:51:14 2018

@author: nisum
"""

import urllib.request, json 
#import sys

job_id = input("Enter the Job ID ")


import urllib

args = print(job_id)
#url = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/{}/wfapi".format(urllib.urlencode(args))
#print(url)

URL = "https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/"
query_string = "/wfapi"

job_url = URL + job_id + query_string

print(job_url)

with urllib.request.urlopen(job_url) as url:
    data = json.loads(url.read().decode('utf-8'))
    
#with open('JSONData.json', 'w') as f:
#    json.dump(data, f)
    
#with open('JSONData.json') as f:
#    json_object = json.load(f)

with open('JSONData.json', 'w') as f:
    json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)
    f.write('\n')
    
#import requests
#
#r = requests.get('https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/5701/wfapi')
#print(r.json())

