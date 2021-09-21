# GWAS-MNER

A GitHub repository dedicated to harbouring all source-code related to my second project at Imperial College London, centred around creating a web-tool which uses data to analyse new data, to scrape some cool metadata!

# About GWAS-MNER

In the context of genome wide association studies (GWAS), reproducibility can prove to be a valuable attribute of the published experiments; this inherently calls for a method to obtain all information necessary to confirm, categorise and potentially reproduce data and results of GWAS. Currently, this curation process is achieved through laborious and time consuming manual identification techniques. New developments in the sphere of machine learning, particularly with natural language processing (NLP) models and algorithms dedicated to data mining and annotating text documents, have presented novel options for the recognition and extraction of key information and metadata from scientific publications. GWAS Metadata Named Entity Recogniser (GWAS-MNER) is the culmination of these advancements; this NLP tool was developed in Python using spaCy 3.0 named entity recognition (NER) as a method for identifying key metadata elements in scientific texts specifically pertinent to GWAS. GWAS-MNER is composed of 5 separate model branches: Platform, Imputation, Total SNPs, Quality Control and Assays. Each branch is able to identify specific metadata elements uniquely, with F1-scores from 0.82-1.00 for the different branches. In essence, GWAS-MNER is intended to serve as a stand-alone web-tool for the extraction of pertinent information from GWAS publications.

Key words: GWAS, Natural Language Processing, Named Entity Recognition, Machine Learning, SNPs

For further information contact nicholas.mcquibban20@imperial.ac.uk.
