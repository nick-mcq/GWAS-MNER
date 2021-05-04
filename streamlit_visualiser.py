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


#nlp = spacy.load('./output/model-best')
#doc = nlp('These samples were assayed with Illumina HumanHap550v3 (N  = 44) and Affymetrix Human610-Quadv1 (N  = 27) arrays.')


#displacy.serve(doc, style="ent")



def model_loader(link,foldername):
  """
  returns path of zipped folder with trained spacy model
  
  """
  import requests
  import zipfile
  import tempfile
  import spacy

  dir=tempfile.gettempdir()


  #link= "https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip"

  results = requests.get(link)
  #with open(dir, 'wb') as f:
  fp = tempfile.TemporaryFile()  
  fp.write(results.content)


  file = zipfile.ZipFile(fp)
  with tempfile.TemporaryDirectory() as tmpdirname:
    file.extractall(path=dir)

  #print(dir)
  end_path=os.path.join(dir, foldername)
  files = os.listdir(end_path)
  #for file in files:
    #print(file)
  return end_path



def main():
    
    """GWAS NLP using SpaCy-Streamlit"""
    st.title("GWAS Metadata Extraction: GWAS MNER")
    menu = ["Home","NER"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
      
      link = 'In order to see the source code for this website, in addition to the code used to develop each branch of the GWAS MNER, you can check out my GitHub repository here: https://github.com/ND2021-ICL/pipe-ABC'
      st.write("""Welcome to my NLP tool, developped to use NER (Named Entity Recognition) as a method for identifying key metadata elements in scientific texts pertinent to GWAS, or Genome Wide Association Studies.""")
      st.markdown(link, unsafe_allow_html=True)
      st.write('')
      st.markdown("""**Use the drop-down menu on the left-hand side of the page to get started!**""")
      st.write('')
      st.write("*Source for sample text used: Stein, J.L., Medland, S.E., Vasquez, A.A., Hibar, D.P., et al. (2012) Identification of common variants associated with human hippocampal and intracranial volumes. Nature genetics. [Online] 44 (5), 552–561. Available from: doi:10.1038/ng.2250.*")
      st.subheader('***Disclaimer:***')
      st.markdown('***The NLP package used in this web-tool originates from SpaCy 3.0, a very recently developped package which makes use of machine learning efficiently and as accurately as possible; however as the word "learning" implies, the algorithm is not perfect and can mistakingly label entities which may "resemble" those it recognises.*** :nerd_face:')
      
    elif choice == "NER":
      st.subheader("Named Entity Recognition")
      # Add a selectbox to the sidebar:
      sel = st.sidebar.selectbox("Which entity would you like to identify?", ["Platform"])
      if sel=="Platform":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp = spacy.load('./output/model-best') #this will change based on which choice was made
      raw_text = st.text_area("Enter text for entity recognition","Total RNA from the middle temporal cortex (Brodmann areas 20 and 21) from 86 subjects was isolated and randomly hybridized to Affymetrix Human Exon 1.0 ST arrays, and quality control analysis was performed using standard methods. The effects of several methodological (day of expression hybridization, RNA integrity number (RIN)) and biological covariates (sex, age and medication) on exon–gene expression relationships were tested for significance. Of these individuals, 71 had participated in a published epilepsy genome-wide association study, and, therefore, genotyping data were available. Details of sample collection and genotyping quality control steps have been published previously66. These samples were assayed with Illumina HumanHap550v3 (N = 44) and Illumina Human610-Quadv1 (N = 27) arrays.")   
      docx = nlp(raw_text)
      spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)  
    
if __name__ == '__main__':
    main()
