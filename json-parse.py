#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:46:36 2018

@author: nisum
"""
obj = []
task_name = []
name = {}

import json

with open('jenkins-log.json', 'r') as log:
    obj = json.load(log)

for tag in obj['stages']:
    name=print(str(tag['name']))
    #name = []
    #name.append(str(tag['name']))
    


#print(type(name))

print(name)






#    for task_name in obj:
#        if task_name == "stages":
#            print(task_name['stages']['name'])
#    print(obj['durationMillis'])
#log.close()



#print(json.load(obj))
#print(obj['name'])