#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:43:14 2021

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
impute_sentences =[]
beagle_sentences =[]
mach_sentences =[]

tuple_list = []



for in_file in PMC_files: #for each PMC M&M file do

    with open(in_file) as m_file:
        
        data = m_file.read()
       
        impute_sentence = re.findall(r"([^.]*?imput[^.]*\.)", data, re.IGNORECASE)
        
        #([^.]*?(i|I)(m|M)(p|P)(u|U)(t|T)[^.]*\.)
        
        impute_sentences += impute_sentence
        
        beagle_sentence = re.findall(r"([^.]*?beagle[^.]*\.)", data, re.IGNORECASE)
        
        beagle_sentences += beagle_sentence
        
        #print(beagle_sentences)
        
        mach_sentence = re.findall(r"([^.]*?mach[^.]*\.)", data, re.IGNORECASE)
        
        mach_sentences += mach_sentence
        
all_sentences = impute_sentences + beagle_sentences + mach_sentences

        #content.append()
        
        
#print(all_sentences)

all_sentences_nodupes = list(set(all_sentences))



#print(all_sentences_nodupes)

#pattern for imput words: (i|I)(m|M)(p|P)(u|U)(t|T)([a-zA-Z\d])+

with open('/project/home20/nam220/NER/NLP/DEV_DATA', 'a') as out_file:
    
    for n in all_sentences_nodupes:
        
        match_imp = re.search(r"(imput[a-zA-Z\d]+)", n) #re.IGNORECASE)
        match_IMPUTE = re.search(r"(IMPUT[a-zA-Z\d]+)", n)
        match_bea = re.search("beagle", n, re.IGNORECASE)
        match_mac = re.search(r"(mach[\d]*)", n, re.IGNORECASE)
        
        
        
        if match_imp:
            #print(match)
            
            #content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation')]})
            #tuple_list.append(content)
            
            if match_bea:
                
                if match_mac:
                    
                    if match_IMPUTE:
                        content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_bea.start(), match_bea.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                        tuple_list.append(content)
            
                    else: 
                        
                        content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_bea.start(), match_bea.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation')]})
                        tuple_list.append(content)
                
                elif match_IMPUTE: 
                    
                    content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_bea.start(), match_bea.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                    tuple_list.append(content)
                
                
                else:
                
                    content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_bea.start(), match_bea.end(), 'imputation')]})
                    tuple_list.append(content)
            
            elif match_mac:
                
                if match_IMPUTE:
                    
                    content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                    tuple_list.append(content)
                
                else:
       
        
                    content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation')]})
                    tuple_list.append(content)
                
            elif match_IMPUTE:
                
                content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                tuple_list.append(content)
            
            else:
                
                content = (n, {'entities': [(match_imp.start(), match_imp.end(), 'imputation')]})
                tuple_list.append(content)
        
        elif match_bea:
            
                if match_mac:
                    
                    if match_IMPUTE:
                    
                        content = (n, {'entities': [(match_bea.start(), match_bea.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                        tuple_list.append(content)
                    
                    else:
            
                        content = (n, {'entities': [(match_bea.start(), match_bea.end(), 'imputation'), (match_mac.start(), match_mac.end(), 'imputation')]})
                        tuple_list.append(content)
                    
                elif match_IMPUTE:
                    
                    content = (n, {'entities': [(match_bea.start(), match_bea.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                    tuple_list.append(content)
                    
                else:
                
                    content = (n, {'entities': [(match_bea.start(), match_bea.end(), 'imputation')]})
                    tuple_list.append(content)
                    
        elif match_mac:
            
            if match_IMPUTE:
                
                content = (n, {'entities': [(match_mac.start(), match_mac.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
                tuple_list.append(content)
            else:
                content = (n, {'entities': [(match_mac.start(), match_mac.end(), 'imputation')]})
                tuple_list.append(content)
        
        elif match_IMPUTE:
            
            content = (n, {'entities': [(match_IMPUTE.start(), match_IMPUTE.end(), 'imputation'), (match_IMPUTE.start(), match_IMPUTE.end(), 'imputation')]})
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

#"/project/home20/nam220/NER/NLP/train.spacy"

stop_time = datetime.datetime.now() #grabs stop time

message = 'Start time is ' + str(start_time) + '\n' + 'Stop time is ' + str(stop_time)  

with open('/project/home20/nam220/NER/NLP/DEV_DATA_runtime.log', 'a') as time_file:   #start and stop time are written into a runtime.log file
    
    #'/project/home20/nam220/NER/AUTOCORPUS_EXTRACT/
    time_file.write(message)
    

    