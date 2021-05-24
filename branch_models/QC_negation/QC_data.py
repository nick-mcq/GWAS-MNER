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

tuple_list = []

all_sentences = []

for in_file in PMC_files: #for each PMC M&M file do

    with open(in_file) as m_file:
        
        data = m_file.read()
       
        QC_sentence = re.findall(r"([^.]*?QC[^.]*\.)", data)
        
        #([^.]*?(i|I)(m|M)(p|P)(u|U)(t|T)[^.]*\.)
        
        all_sentences += QC_sentence
        
        quality_sentence = re.findall(r"([^.]*?quality control[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += quality_sentence
        
        #print(beagle_sentences)
        
        minor_sentence = re.findall(r"([^.]*?minor allele[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += minor_sentence
        
        
        MAF_sentence = re.findall(r"([^.]*?MAF[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += MAF_sentence
        
        PLINK_sentence = re.findall(r"([^.]*?PLINK ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += PLINK_sentence
        
        PLATO_sentence = re.findall(r"([^.]*?PLATO ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += PLATO_sentence
        
        QUICK_sentence = re.findall(r"([^.]*?QUICKTEST ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += QUICK_sentence
        
        SOLAR_sentence = re.findall(r"([^.]*?SOLAR ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += SOLAR_sentence
        
        eig_sentence = re.findall(r"([^.]*?eigensoft ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += eig_sentence
        
        SNP_sentence = re.findall(r"([^.]*?SNPTEST ?[v\d.\d?]*[^.]*\.)", data, re.IGNORECASE)
        
        all_sentences += SNP_sentence
        
#all_sentences = impute_sentences + beagle_sentences + mach_sentences

        #content.append()
        
        
#print(all_sentences)

all_sentences_nodupes = list(set(all_sentences))



#print(all_sentences_nodupes)


with open('/project/home20/nam220/NER/NLP/DEV_DATA', 'a') as out_file:
    
    #/project/home20/nam220/NER/NLP/
    
    for n in all_sentences_nodupes:
        
        entity_list = []
        
        match_QC = re.search(r"(QC)", n) #re.IGNORECASE)
        match_quality = re.search(r"(quality control)", n, re.IGNORECASE)
        match_minor = re.search("(minor allele frequency)", n, re.IGNORECASE)
        match_MAF = re.search(r"(MAF)", n, re.IGNORECASE)
        match_PLINK = re.search(r"(PLINK)", n, re.IGNORECASE)
        match_PLATO = re.search(r"(PLATO)", n, re.IGNORECASE)
        match_QUICKTEST = re.search(r"(QUICKTEST)", n, re.IGNORECASE)
        match_SOLAR = re.search(r"(SOLAR)", n)
        match_eig = re.search(r"(eigensoft)", n, re.IGNORECASE)
        match_SNP = re.search(r"(SNPTEST)", n)
        
        
        
        match_V = re.search(r"(v\d+[.]?\d+)", n, re.IGNORECASE)
        
        match_no = re.search(r"(?:^|\W)no(?:$|\W)", n, re.IGNORECASE)
        match_not = re.search(r"(?:^|\W)not(?:$|\W)", n, re.IGNORECASE)
        match_non = re.search(r"(non-)", n, re.IGNORECASE)
        
        
        if match_QC:
            #print(match)
            
            info = (match_QC.start(), match_QC.end(), 'quality control')
            entity_list.append(info)
        
        
        if match_quality:
            
            info = (match_quality.start(), match_quality.end(), 'quality control')
            entity_list.append(info)
            
            
        if match_minor:
            
            info = (match_minor.start(), match_minor.end(), 'quality control')
            entity_list.append(info)
        
        if match_MAF:
            
            info = (match_MAF.start(), match_MAF.end(), 'quality control')
            entity_list.append(info)
        
        
        if match_PLINK:
            
            info = (match_PLINK.start(), match_PLINK.end(), 'quality control')
            entity_list.append(info)
        
        if match_PLATO:
            
            info = (match_PLATO.start(), match_PLATO.end(), 'quality control')
            entity_list.append(info)
            
        if match_QUICKTEST:
            
            info = (match_QUICKTEST.start(), match_QUICKTEST.end(), 'quality control')
            entity_list.append(info)
        
        
        if match_SOLAR:
            
            info = (match_SOLAR.start(), match_SOLAR.end(), 'quality control')
            entity_list.append(info)
        
        if match_eig:
            
            info = (match_eig.start(), match_eig.end(), 'quality control')
            entity_list.append(info)
            
        if match_SNP:
            
            info = (match_SNP.start(), match_SNP.end(), 'quality control')
            entity_list.append(info)
            
        if match_V:
            
            info = (match_V.start(), match_V.end(), 'version number')
            entity_list.append(info)
            
        if match_non:
            
            info = (match_non.start(), match_non.end(), 'negation')
            entity_list.append(info)     
            
            
        if match_no:
            
            info = (match_no.start()+1, match_no.end()-1, 'negation')
            entity_list.append(info)
            
        if match_not:
            
            info = (match_not.start()+1, match_not.end()-1, 'negation')
            entity_list.append(info)
        
        
        content = (n, {'entities': entity_list})
            
        tuple_list.append(content)
        

    print(tuple_list)        

    
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
    
    #'/project/home20/nam220/NER/NLP/
    time_file.write(message)

