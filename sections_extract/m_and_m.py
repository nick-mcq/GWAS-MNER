# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import json
import datetime

start_time = datetime.datetime.now() #grabs start time

supp =[] #empty list for PMCIDS of texts containing supplementary data

message = '' #empty string to hold message with time in it

PMC_files=[] #empty list to hold all PMC filenames in it for iteration

all_files = os.listdir() #make sure to run this algorithm in the directory containing the PMCID.json files

for n in all_files:
    
    if n.startswith('PMC'):  #gets a list of every PMC file in the directory
        PMC_files.append(n)

#print(PMC_files)

for in_file in PMC_files: #for each PMC json file, do this
    
    body =''
    PMCID=in_file[0:10]  #stores the PMCID of the paper for output prefix
    

    with open(in_file) as json_file:
        data = json.load(json_file)
    
        #print(data)
    
        paragraphs = (data['paragraphs']) #3 dictionaries at first level, grab the paragraphs one only
    
        for i in paragraphs:
        
            if 'IAO_0000633' in [x for v in i.values() for x in v] or 'IAO_0000317' in [x for v in i.values() for x in v]:
           
                body += (i['body'])        #either IAO ID is checked for, making sure to iterate in a way which checks inside lists of IAO_ID
           
            elif 'IAO_0000326' in [x for v in i.values() for x in v]:
        
                supp.append(PMCID) #here the list of files which have a supplementary will be aggregated
           
           
    with open(f'/project/home20/nam220/NER/AUTOCORPUS_EXTRACT/DEV_METHODS/{PMCID}.txt', 'a') as output: #f-string used to create output name
        output.write(body)
    
    
with open('/project/home20/nam220/NER/AUTOCORPUS_EXTRACT/DEV_MAINTEXT/supp.log', 'a') as supp_file: #PMC papers with supplementary data stored in list
    supp_file.write(str(supp))
    
    
stop_time = datetime.datetime.now() #grabs stop time

message = 'Start time is ' + str(start_time) + '\n' + 'Stop time is ' + str(stop_time)  

with open('/project/home20/nam220/NER/AUTOCORPUS_EXTRACT/DEV_MAINTEXT/m_and_m_runtime.log', 'a') as time_file:   #start and stop time are written into a runtime.log file
    
    
    time_file.write(message)
          
    
'''

For later

  1.  
    load master list into dataframe, match the file PMCID to the master, check that the master platform is in body. 
    if the platform is not in body, mark down the inconsistency
    
    
    if 'Illumina' not in body:
        print('Inconsistency with master list detected')

    
'''
