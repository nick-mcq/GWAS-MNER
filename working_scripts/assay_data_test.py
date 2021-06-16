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
       
        illumina_sentence = re.findall(r"([^.]*?Illumina[^.]*\d.\d*[^.]*.)", data)
        
        all_sentences += illumina_sentence
        
        affymetrix_sentence = re.findall(r"([^.]*?Affymetrix[^.]*\d.\d*[^.]*.)", data)
        
        all_sentences += affymetrix_sentence
        
        perlegen_sentence = re.findall(r"([^.]*?Perlegen[^.]*\d.\d*[^.]*.)", data)
        
        all_sentences += perlegen_sentence
        
#all_sentences = impute_sentences + beagle_sentences + mach_sentences

        #content.append()
        
        
#print(all_sentences)

all_sentences_nodupes = list(set(all_sentences))

#print(all_sentences_nodupes)

with open('TEST_DATA6', 'a') as out_file:
    
    #/project/home20/nam220/NER/NLP/
    
    for n in all_sentences_nodupes:
        
        if " or " in n:
            
            continue
        
        if " Array Sets " in n:
            
            continue
        
        if "(Illumina)" in n:
            
            continue
        
        if "(Affymetrix)" in n:
            
            continue
        
        if "(Supplementary Table 4)" in n:
            
            continue
        
        if 'KhoeSan' in n:
            continue
        
        if "GSE21032" in n:
            continue
        
        if "ITMAT-Broad-CARe (IBC)" in n:
            continue
        
        if "(GINIplus and LISAplus)" in n:
            continue
        if "Both discovery and replication cohorts were genotyped on a variety of platforms" in n:
            continue
        
        if "FinnDiane Study" in n:
            
            continue
        
        if "(see  Table E5)" in n:
            continue
        
        if "Affymetrix Axiom, Illumina 550k, custom Illumina Immunochip" in n:
            
            continue
        if "Sequenom MassARRAY platform" in n:
            continue
        
        if "PopGen samples were typed on" in n:
            continue
        
        if "we used 1958 Birth Cohorts and UK Blood Service control data" in n:
            continue
        
        if "(Swedish sample 1)" in n:
            continue
        
        if "(Supplementary Material, Table S1)" in n:
            
            continue
        
        if "genotyping was done on a variety of platforms" in n:
            continue
        
        if "B58C" in n:
            continue
        
        if "MONICA-KORA" in n:
            continue
        
        if "and a 50,000 SNP custom Illumina chip (FHS)" in n:
            continue
        
        if "array not present on the Affymetrix" in n:
            continue
        
        if "Kooperative Gesundheitsforschung" in n:
            continue
        
        if "HapMap Phase 3 CHB samples" in n:
            continue
        
        if "32 Stage 1 studies" in n:
            continue
        
        if "three-step algorithm out" in n:
            continue
        
        if "and 84 SNPs overlapped" in n:
            continue
        
        if "PARD3B region" in n:
            continue
        
        
        
        entity_list = []
        
        match_Iplat = re.search(r"(Illumina.*?platform[s]?)", n, re.IGNORECASE)
        match_IaN = re.search(r"(Illumina.*?array[s]?.\d[.]?\d)", n, re.IGNORECASE)
        match_Ia = re.search("(Illumina.*?array[s]?)", n, re.IGNORECASE)
        match_Ic = re.search(r"(Illumina.*? chip[s]?)", n, re.IGNORECASE)
        match_IBC = re.search(r"(Illumina.*?beadchip[s]?)", n, re.IGNORECASE)
        match_IK = re.search(r"(Illumina.\d+.?[K])", n, re.IGNORECASE)
        match_IW = re.search(r"(Illumina.\d+.?[W])", n, re.IGNORECASE)
        
        
        match_Ac = re.search(r"(Affymetrix.*? chip[s]?)", n, re.IGNORECASE)
        match_AaN = re.search(r"(Affymetrix.*?array[s]?.\d[.]?\d)", n, re.IGNORECASE)
        match_Aa = re.search(r"(Affymetrix.*?array[s]?)", n, re.IGNORECASE)
        match_Aplat = re.search(r"(Affymetrix.*?platform[s]?)", n, re.IGNORECASE)
        match_AK = re.search(r"(Affymetrix.\d+.?[K])", n, re.IGNORECASE)
        
        match_Pc = re.search(r"(Perlegen.*? chip[s]?)", n, re.IGNORECASE)
        match_PK = re.search(r"(Perlegen.\d+.?[K])", n, re.IGNORECASE)
        
        
        
        match_V = re.search(r"(v\d+[.]?\d+)", n, re.IGNORECASE)
        
        
        if match_Iplat:
            #print(match)
            
            info = (match_Iplat.start(), match_Iplat.end(), 'Illumina assay')
            entity_list.append(info)
            
        elif match_IBC:
            
            info = (match_IBC.start(), match_IBC.end(), 'Illumina assay')
            entity_list.append(info)
        
        
        elif match_IaN:
            
            info = (match_IaN.start(), match_IaN.end(), 'Illumina assay')
            entity_list.append(info)
            
            
        elif match_Ia:
            
            info = (match_Ia.start(), match_Ia.end(), 'Illumina assay')
            entity_list.append(info)
        
        elif match_Ic:
            
            info = (match_Ic.start(), match_Ic.end(), 'Illumina assay')
            entity_list.append(info)
        
        
        elif match_IK:
            
            info = (match_IK.start(), match_IK.end(), 'Illumina assay')
            entity_list.append(info)
            
        elif match_IW:
            
            info = (match_IW.start(), match_IW.end(), 'Illumina assay')
            entity_list.append(info)
        
        if match_Ac:
            
            info = (match_Ac.start(), match_Ac.end(), 'Affymetrix assay')
            entity_list.append(info)
            
        elif match_AaN:
            
            info = (match_AaN.start(), match_AaN.end(), 'Affymetrix assay')
            entity_list.append(info)
            
        elif match_Aa:
            
            info = (match_Aa.start(), match_Aa.end(), 'Affymetrix assay')
            entity_list.append(info)
            
        elif match_Aplat:
            
            info = (match_Aplat.start(), match_Aplat.end(), 'Affymetrix assay')
            entity_list.append(info)
        
        elif match_AK:
            
            info = (match_AK.start(), match_AK.end(), 'Affymetrix assay')
            entity_list.append(info)
            
            
        if match_Pc:
            
            info = (match_Pc.start(), match_Pc.end(), 'Perlegen assay')
            entity_list.append(info)
            
        elif match_PK:
            
            info = (match_PK.start(), match_PK.end(), 'Perlegen assay')
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

db.to_disk("/project/home20/nam220/NER/NLP/test.spacy") # save the docbin object

#"/project/home20/nam220/NER/NLP/train.spacy"

stop_time = datetime.datetime.now() #grabs stop time

message = 'Start time is ' + str(start_time) + '\n' + 'Stop time is ' + str(stop_time)  

with open('/project/home20/nam220/NER/NLP/TEST_DATA_runtime.log', 'a') as time_file:   #start and stop time are written into a runtime.log file
    
    #'/project/home20/nam220/NER/NLP/
    time_file.write(message)
