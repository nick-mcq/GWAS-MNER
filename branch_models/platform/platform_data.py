#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:10:17 2021

@author: nicholasmcquibban
"""

import os
import regex as re
import datetime


import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin


start_time = datetime.datetime.now() #grabs start time

message = '' #empty string to hold message with time in it

PMC_files=[] #empty list to hold all PMC filenames in it for iteration

all_files = os.listdir() #make sure to run this algorithm in the directory containing the PMCID.txt files

for n in all_files:
    
    if n.startswith('PMC'):  #gets a list of every PMC file in the directory
        PMC_files.append(n)

content = ()
illumina_sentences =[]
affymetrix_sentences =[]
perlegen_sentences =[]

tuple_list = []



for in_file in PMC_files: #for each PMC M&M file do

    with open(in_file) as m_file:
        
        data = m_file.read()
       
        illumina_sentence = re.findall(r"([^.]*?Illumina[^.]*\d.\d*[^.]*.)", data)
        
        illumina_sentences += illumina_sentence
        
        affymetrix_sentence = re.findall(r"([^.]*?Affymetrix[^.]*\d.\d*[^.]*.)", data)
        
        affymetrix_sentences += affymetrix_sentence
        
        perlegen_sentence = re.findall(r"([^.]*?Perlegen[^.]*\d.\d*[^.]*.)", data)
        
        perlegen_sentences += perlegen_sentence
        
all_sentences = illumina_sentences + affymetrix_sentences + perlegen_sentences

        #content.append()

all_sentences_nodupes = list(set(all_sentences))

#print(all_sentences_nodupes)

with open('DEV_DATA', 'a') as out_file:
    
    for n in all_sentences:
        
        
        I_count = n.count('Illumina')
        A_count = n.count('Affymetrix')
        P_count = n.count('Perlegen')
        
        
        if 'Illumina' in n and I_count <=1 and A_count == P_count == 0:
            
            match = re.search('Illumina', n) 
            
            #print(match)
            
            content = (n, {'entities': [(match.start(), match.end(), 'platform')]})
            tuple_list.append(content)
            
        elif 'Affymetrix' in n and A_count <=1 and I_count == P_count == 0:
            
            match = re.search('Affymetrix', n) 
            
            content = (n, {'entities': [(match.start(), match.end(), 'platform')]})
            tuple_list.append(content)
            
        elif 'Perlegen' in n and P_count <=1 and A_count == 1:
            
            match = re.search('Perlegen', n) 
            
            content = (n, {'entities': [(match.start(), match.end(), 'platform')]})
            tuple_list.append(content)
            
        
    
    for element in tuple_list:
        
        if element == tuple_list[0]:
            
            out_file.write('[')
            out_file.write(str(element))
            out_file.write(',')
            out_file.write('\n')
            
        elif element == tuple_list[-1]:
            
            out_file.write(' ')
            out_file.write(str(element))
            out_file.write(']')
        
        else:
       
            out_file.write(' ')
            out_file.write(str(element))
            out_file.write(',')
            out_file.write('\n')
       
 
    #print(content[0])

#('Full sentence appears here.', {'entities': [(start, stop, 'platform')]})

#old regex formula: ([^.]*?Perlegen[^.]*\.)
    
    
nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object

DEV_DATA = tuple_list

for text, annot in tqdm(DEV_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("/project/home20/nam220/NER/NLP/train.spacy") # save the docbin object

stop_time = datetime.datetime.now() #grabs stop time

message = 'Start time is ' + str(start_time) + '\n' + 'Stop time is ' + str(stop_time)  

with open('/project/home20/nam220/NER/AUTOCORPUS_EXTRACT/DEV_DATA_runtime.log', 'a') as time_file:   #start and stop time are written into a runtime.log file
    
    
    time_file.write(message)
    




