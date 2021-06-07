#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:40:55 2021

@author: nicholasmcquibban
"""

import spacy
import os
import streamlit as st
import spacy_streamlit
import json

#nlp = spacy.load('./output/model-best')
#doc = nlp('These samples were assayed with Illumina HumanHap550v3 (N  = 44) and Affymetrix Human610-Quadv1 (N  = 27) arrays.')


#displacy.serve(doc, style="ent")





def main():
    
    
    
    st.set_page_config(page_title="Project 2: GWAS-MNER",page_icon=":floppy_disk:",layout="centered",initial_sidebar_state="expanded")
    
    st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)
  
    st.title("GWAS Metadata Extraction: GWAS MNER")
    choice = st.sidebar.selectbox("Navigate to", ["Project Report","NER web-tool"])
    st.sidebar.write('')
    st.sidebar.write('')
     
    if choice == "Project Report":
        
      st.header("Welcome! \n Use the drop-down menu on the left-hand side of the page to access the **NER (named entity recognition) web-tool**. This tool uses **NLP (natural language processing) software** to develop models which identify key elements or words in user-inputted text, based on training and testing data obtained from 1200 papers focussed on **GWAS (genome wide association studies)**.  \n\n Alternatively, click on the checkboxes to reveal one or multiple sections of the **project report**. Please note that the web-page will **NOT** scroll automatically when **revealing multiple sections**.")
   
    
      empty=True
        
      
      
      if st.sidebar.checkbox("Introduction"):
        
        st.subheader("Introduction & Motivation")
        
    
        st.markdown("In layman terms, the GWAS-MNER web-tool is a 'smart' algorithm which has been exposed to hundreds of PubMed articles containing specifically labelled words for the algorithm to recognise, and importantly, remember. Indeed, once it has learned these important words, known as entities, it can then attempt to read a new piece of text (submitted by you) and recognise any of those previously memorised entities! Further, this algorithm falls under a category known as machine learning, meaning that it is also capable of making an educated guess at what *might* be an entitity, if it deems the word(s) to resemble those it already knows. Finally, the publications used to train and test GWAS-MNER models, of which there are 5 (each model is dedicated to a specific metadata category), are all GWAS publications, as this was the area of research targeted by the project.")
      
        st.markdown("The design of this user-friendly web-tool was driven by a lack of easily deployable automated methods for grouping and extracting relevant information of interest in GWAS publications; as the creator of the tool and author of this report, I learned during my undergraduate years in molecular genetics that it was notoriously laborious to sift through swathes of GWAS publications manually in search of key methods, such as which assays were used or what kind of quality control was applied. Moreover, this machine was also developped to showcase the power of text extraction software known as AutoCORPus (Automated and Consistent Outputs from Research Publications), an automated pipeline which can parse through PubMed publications, for example, organising the text into a single JSON output split by relevant sections (Hu et al., 2021).")
        empty=False
        
      if st.sidebar.checkbox("Methods & Materials"):
        
        st.subheader("Methods")
        
    
        st.markdown("**General workflow of Project 2: GWAS-MNER**  \n\n.")
      
        empty=False
        
      if st.sidebar.checkbox("Results"):
        
        st.subheader("Results")
        
    
        st.markdown("The resulting NER branches were scored for their overall accuracy in evalutaing second testing set, after learning from the inital testing set. A bar chart was generated to illustrate and compare the scores of each branch model")
    
        empty=False
    
      if st.sidebar.checkbox("Discussion"):
        
        st.subheader("Discussion")
        
    
        st.markdown("The accuracy of a branch can be directly correlated with the complexity of the entity with which a label is associated, as it results in more likely cases of confusion within the algorithms predetermined parameters. However, these are all variables which can be adjusted by the developper, which points towards potential for perfecting, when there is sufficient time to do so. Overall, the use of NLP and NER in particular could prove hugely valuable in automatically scraping key data for further work or documentation; the important distinction to be made in the case of this tool is that which data the user requests is customisable, opening up new possibilities in terms of user-orientated machine learning-driven results")
    
        empty=False
    
      if st.sidebar.checkbox("Future Work"):
        
        st.subheader("Future Work")
        
    
        st.markdown("Due to the time constraints imposed upon this project, an initially proposed multi-model version of the algorithm was not produced, such that it would combine all branches into one algorithm searching for all entities simultaneously. Further, the lack of data in regards to Perlegen assays proved detrimental in providing the algorithm with sufficient data for recognising such assays. Overall, there is room for improvement in every single branch; expanding the datasets fed into the program would prove valuable in furthering the capabilities of GWAS-MNER.")
    
        empty=False
        
      if st.sidebar.checkbox("Conclusion"):
        
        st.subheader("Conclusion")
        
    
        st.markdown("In conclusion, this web-tool was developed using the output produced from the AutoCORPus program (reference needed), following an extensive curation and refinement process, to learn and accurately label key metadata in any scientific text on the topic of GWAS. Moreover, this process could be adapted for publications covering other topics, or even multiple topics, based on how much data is fed into the NLP algorithm.")
    
        empty=False
    
      if st.sidebar.checkbox("References"):
        
        st.subheader("References")
        
    
        st.markdown("The following references were used in this project:")
    
        empty=False
        
      if empty==True:
          
          st.subheader("Abstract")

          link = 'Source code: https://github.com/nick-mcq/GWAS-MNER'
          st.write("""In the context of genome wide association studies (GWAS), reproducibility can prove to be a valuable attribute of the published experiments; this inherently calls for a method to obtain all information necessary to confirm, categorise and potentially reproduce data and results of GWAS. New developments in the sphere of machine learning, particularly with natural language processing (NLP) models and algorithms, dedicated to data mining and annotating text documents have presented novel options for the recognition and extraction of key information and metadata from scientific publications. GWAS-MNER is the culmination of these advancements; this NLP tool was developed in Python using spaCy 3.0 named entity recognition (NER) as a method for identifying key metadata elements in scientific texts specifically pertinent to GWAS. This report highlights the development and capabilities of GWAS-MNER, a stand-alone web-tool for the extraction of pertinent information from GWAS publications. """)
          st.markdown(link, unsafe_allow_html=True)
          #st.write('')
          
      
    
    elif choice == "NER web-tool":
      st.subheader("Named Entity Recognition")
      # Add a selectbox to the sidebar:
      sel = st.sidebar.selectbox("Which entity would you like to identify?", ["Platform", "Imputation", 'Total SNPs', 'Quality Control', 'Assays'])
      if sel=="Platform":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp1 = spacy.load('/Users/nicholasmcquibban/Desktop/branch_outputs/platform/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","Total RNA from the middle temporal cortex (Brodmann areas 20 and 21) from 86 subjects was isolated and randomly hybridized to Affymetrix Human Exon 1.0 ST arrays, and quality control analysis was performed using standard methods. The effects of several methodological (day of expression hybridization, RNA integrity number (RIN)) and biological covariates (sex, age and medication) on exon–gene expression relationships were tested for significance. Of these individuals, 71 had participated in a published epilepsy genome-wide association study, and, therefore, genotyping data were available. Details of sample collection and genotyping quality control steps have been published previously66. These samples were assayed with Illumina HumanHap550v3 (N = 44) and Illumina Human610-Quadv1 (N = 27) arrays.", help="Sample text source: Stein, J.L., Medland, S.E., Vasquez, A.A., Hibar, D.P., et al. (2012)")   
         docx = nlp1(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp1.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD"):
             
             
             with open('GWASMNER_Platform.json', 'w') as json_file:
                
                 
                json.dump(docx.to_json(), json_file)
            
             with open('GWASMNER_Platform_Trimmed.json', 'w') as dest_file:
                 with open('GWASMNER_Platform.json', 'r') as source_file:
                     for line in source_file:
                         element = json.loads(line.strip())
                         if 'tokens' in element:
                             del element['tokens']
                         dest_file.write(json.dumps(element))
             
            
             
      if sel=="Imputation":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp2 = spacy.load('/Users/nicholasmcquibban/Desktop/branch_outputs/imputation_negation/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","To validate additional associated SNPs (p < 0.0001) and nominally associated candidate genes, we imputed SNPs from our GWAS using a previously published GWAS1 along with both the IMPUTE and BEAGLE programs. In addition another study, which did not impute any further SNPs, served to further validate our results for candidate genes (see Supplementary Table 5) ")   
         docx = nlp2(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp2.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD"):
             
             
             with open('GWASMNER_Imputation.json', 'w') as json_file:
                
                 
                json.dump(docx.to_json(), json_file)
            
             with open('GWASMNER_Imputation_Trimmed.json', 'w') as dest_file:
                 with open('GWASMNER_Imputation.json', 'r') as source_file:
                     for line in source_file:
                         element = json.loads(line.strip())
                         if 'tokens' in element:
                             del element['tokens']
                         dest_file.write(json.dumps(element)) 
         
         
         
      if sel=="Total SNPs":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp3 = spacy.load('/Users/nicholasmcquibban/Desktop/branch_outputs/SNP#/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","We based our further analyses on 2,168,847 SNPs that met imputation and genotyping QC criteria across all studies (Methods; Supplementary Methods). We then conducted a series of association analyses to relate the 2.2 million genotyped and/or imputed SNPs with plasma concentrations of HDL cholesterol, LDL cholesterol and triglyceride concentrations. ")   
         docx = nlp3(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp3.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD"):
             
             
             with open('GWASMNER_SNP.json', 'w') as json_file:
                
                 
                json.dump(docx.to_json(), json_file)
            
             with open('GWASMNER_SNP_Trimmed.json', 'w') as dest_file:
                 with open('GWASMNER_SNP.json', 'r') as source_file:
                     for line in source_file:
                         element = json.loads(line.strip())
                         if 'tokens' in element:
                             del element['tokens']
                         dest_file.write(json.dumps(element))
         
         
         
      if sel=="Quality Control":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp4 = spacy.load('/Users/nicholasmcquibban/Desktop/branch_outputs/QC/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","Quality control of genotype data and genetic association analyses were performed using PLINK v1.07 ().")   
         docx = nlp4(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp4.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD"):
             
             
             with open('GWASMNER_QC.json', 'w') as json_file:
                
                 
                json.dump(docx.to_json(), json_file)
            
             with open('GWASMNER_QC_Trimmed.json', 'w') as dest_file:
                 with open('GWASMNER_QC.json', 'r') as source_file:
                     for line in source_file:
                         element = json.loads(line.strip())
                         if 'tokens' in element:
                             del element['tokens']
                         dest_file.write(json.dumps(element))
         
         
      if sel=="Assays":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp5 = spacy.load('/Users/nicholasmcquibban/Desktop/branch_outputs/assay_total/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","The 529 LCLs derived from the CAP cohort were incubated under standardized conditions for 24hr, after which MGMT transcript levels were quantified using the Illumina H8v3 beadarray. Individuals in the WHI-SHARe cohort were genotyped on the Affymetrix 6.0 array.")   
         docx = nlp5(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp5.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD"):
             
             
             with open('GWASMNER_Assays.json', 'w') as json_file:
                
                 
                json.dump(docx.to_json(), json_file)
            
             with open('GWASMNER_Assays_Trimmed.json', 'w') as dest_file:
                 with open('GWASMNER_Assays.json', 'r') as source_file:
                     for line in source_file:
                         element = json.loads(line.strip())
                         if 'tokens' in element:
                             del element['tokens']
                         dest_file.write(json.dumps(element))
         
         
         
      if st.button("DISCLAIMER", help="Press me to see a quick disclaimer regarding the SpaCy 3.0 software!"):
      
      
         st.error('***The NLP package used in this web-tool originates from SpaCy 3.0, a very recently developped package which makes use of machine learning efficiently and as accurately as possible; however as the word "learning" implies, the algorithm is not perfect and can mistakingly label entities which may "resemble" those it recognises.*** :nerd_face:')
      
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
