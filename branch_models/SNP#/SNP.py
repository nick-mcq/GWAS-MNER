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
onecomma_sentences =[]
twocomma_sentences =[]
million_sentences =[]

tuple_list = []



for in_file in PMC_files: #for each PMC M&M file do

    with open(in_file) as m_file:
        
        data = m_file.read()
       
        onecomma_sentence = re.findall(r"([^.]*? [0-9]+,[0-9]+ S?N?P?s?[^.]*.)", data)
        
        onecomma_sentences += onecomma_sentence
        
        
        twocomma_sentence = re.findall(r"([^.]*?[0-9]+,[0-9]+,[0-9]+ ?S?N?P?s?[^.]*.)", data)
        
        twocomma_sentences += twocomma_sentence
        
        
        million_sentence = re.findall(r"([^.]*?[0-9][0-9.]+ ?million ?S?N?P?[^.]*?)", data, re.IGNORECASE)
        
        million_sentences += million_sentence
        
all_sentences = onecomma_sentences + twocomma_sentences + million_sentences

        #content.append()
 
#print(all_sentences)
all_sentences_nodupes = list(set(all_sentences))

all_sentences_SNP = [item for item in all_sentences_nodupes if 'SNP' in item]

all_sentences_singleNP = [item for item in all_sentences_nodupes if 'single nucleotide polymorphism' in item]

final_sentences = all_sentences_SNP + all_sentences_singleNP

print(final_sentences)


#print(all_sentences_nodupes)

with open('/project/home20/nam220/NER/NLP/DEV_DATA', 'a') as out_file:
    
    #/project/home20/nam220/NER/NLP/
    
    for n in final_sentences:
        
        
        if len(re.findall(r"([^.]*? [0-9]+,[0-9]+ S?N?P?s?[^.]*.)", n)) <= 1 and len(re.findall(r"([^.]*?[0-9]+,[0-9]+,[0-9]+ ?S?N?P?s?[^.]*.)", n)) <= 1 and len(re.findall(r"([^.]*?[0-9][0-9.]+ ?million ?S?N?P?[^.]*?)", n, re.IGNORECASE)) <= 1:
        
            match_one = re.search(r" ([0-9]+,[0-9]+) ", n)
            match_two = re.search(r"([0-9]+,[0-9]+,[0-9]+)", n)
            match_mil = re.search(r"([0-9][0-9.]+ ?million)", n, re.IGNORECASE)
        
        
        
            if match_one:
            #print(match)
            
                if match_two:
                    
                    if match_mil:
                        
                        content = (n, {'entities': [(match_one.start()+1, match_one.end()-1, 'Total SNPs'), (match_two.start(), match_two.end(), 'Total SNPs'), (match_mil.start(), match_mil.end(), 'Total SNPs')]})
                        tuple_list.append(content)
                        
                    else: 
                        
                        content = (n, {'entities': [(match_one.start()+1, match_one.end()-1, 'Total SNPs'), (match_two.start(), match_two.end(), 'Total SNPs')]})
                        tuple_list.append(content)
            
                elif match_mil:
                    
                    content = (n, {'entities': [(match_one.start()+1, match_one.end()-1, 'Total SNPs'), (match_mil.start(), match_mil.end(), 'Total SNPs')]})
                    tuple_list.append(content)
                    
                else:
            
                    content = (n, {'entities': [(match_one.start()+1, match_one.end()-1, 'Total SNPs')]})
                    tuple_list.append(content)
            
            elif match_two:
                
                if match_mil:
                    
                    content = (n, {'entities': [(match_two.start(), match_two.end(), 'Total SNPs'), (match_mil.start(), match_mil.end(), 'Total SNPs')]})
                    tuple_list.append(content)
       
                else:
       
                    content = (n, {'entities': [(match_two.start(), match_two.end(), 'Total SNPs')]})
                    tuple_list.append(content)
                    
            elif match_mil:
                
                content = (n, {'entities': [(match_mil.start(), match_mil.end(), 'Total SNPs')]})
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
    
    #'/project/home20/nam220/NER/NLP/
    time_file.write(message)
