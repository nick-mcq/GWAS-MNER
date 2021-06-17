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
import altair as alt
import pandas as pd

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
        
      st.header("Welcome: Website Navigation & Lay Summary \n Use the drop-down menu on the left-hand side of the page to access the **NER (named entity recognition) web-tool**. This tool uses **NLP (natural language processing) software** to develop models which identify key elements or words in user-inputted text, based on training and testing data obtained from 1200 papers focussed on **GWAS (genome wide association studies)**.  \n\n Alternatively, click on the checkboxes to reveal one or multiple sections of the **project report**. Please note that the web-page will **NOT** scroll automatically when **revealing multiple sections**. \n\n Simply put, GWAS-MNER is a machine learning algorithm which has been trained and tested to detect key words of interest, specifically in the context of Genome Wide Association Studies (GWAS). This algorithm was split up into 5 separate parts, each of which can identify its own set of key words. Examples of such words include examples of quality control (QC) techniques, or the names of important companies involved in GWAS results. Importantly, not only does the algorithm recognise words which it has already been shown in training data, but it can also make an educated guess at what *may* be a key term if it resembles what it has learned. Once an important word or set of words is identified by the algorithm, it labels the start and end positions of the target (also known as 'entity'). This project highlights the potential of automation in the curation of large amounts of scientific data.")
   
    
      empty=True
        
      
      
      if st.sidebar.checkbox("Introduction"):
        
        st.subheader("Introduction & Motivation")
        
    
        st.markdown("The lack of automation in the annotation and extraction of key elements in scientific publications, particularly in the realm of genome-wide association studies (GWAS), calls for the development of a functional tool which can replace the currently laborious, manual curation methods in place for data-driven scientists (Pandey et al., 2012). In essence, the GWAS Metadata Named Entity Recogniser (GWAS-MNER) web-tool is a 'smart' algorithm which has been exposed to hundreds of PubMed articles containing specifically labelled words for the algorithm to recognise, and importantly, remember. Indeed, once it has learned these important words, known as entities, it can then receive a new piece of text (submitted by the user) and analyse it using the knowledge/model from the labelled data set to predict which words can be considered entities of interest. Further, this algorithm falls under a category known as machine learning, meaning that it is also capable of making an educated guess at what *might* be an entitity, if it deems the word(s) to resemble those it already knows enough (Lee et al., 2020). Structurally, GWAS-MNER consists of 5 separate model branches, each of which has been carefully curated and taught to recognise unique entities of interest: the 'Platform' branch identifies which company developed the assays of interest, the 'Imputation' branch looks for all mention of single nucleotide polymorphism (SNP) imputation methods and information, the 'Total SNPs' branch identifies the number of SNP variants tested in a study, the 'Quality Control' branch labels any mention of quality control (QC) or quality control software, and the 'Assays' branch attempts to identify the full complex assays used in the GWAS study of interest. Finally, the publications used to train and test GWAS-MNER models are all GWAS publications, as this was the area of research targeted by the project.")
      
        st.markdown("The design of this user-friendly web-tool was driven by a lack of easily deployable automated methods for grouping and extracting relevant information of interest in GWAS publications; undergraduate students and genomic scientists alike all are well aware of the laborious task of sifting through swathes of GWAS publications manually in search of key methods, such as which assays were used or what kind of quality control was applied. Moreover, this web-tool was also developed to showcase the power of text extraction software known as AutoCORPus (Automated and Consistent Outputs from Research Publications), an automated pipeline which can parse through PubMed publications, for example, organising the text into a single JSON output split by relevant sections (Hu et al., 2021); this categorisation of publications allowed for the straightforward extraction and concatenation of the most relevant sections, which in this case was the Methods & Materials text.")
        
        if st.button("Introduction Glossary", help = 'Press me to reveal a glossary defining some key terms used in this section'):
            
            st.warning('**GWAS**: A genome-wide association study, also called whole genome association study or GWAS, is an investigative study of numerous genetic variants, namely SNPs, in a cohort of individuals; the goal is to identify whether any variants are linked to a certain trait, such as a disease for example. \n\n **SNP**: A single nucleotide polymorphism (SNP) is a substitution, deletion or addition of a single nucleotide at a specific position in the genome. \n\n **Imputation**: Imputation in genetics refers to the statistical inference of experimentally unidentified genotypes, particularly used for inferring the location of specific SNPs in a GWAS study. \n\n **JSON**: JavaScript Object Notation (JSON) is an open source, standardised file format and data rearrangement format that converts plaintext into data elements consisting of attribute–value pairs, such that data can be stored and accessed using list comprehension and dictionaries.  ' )
        
        empty=False
        
      if st.sidebar.checkbox("Methods & Materials"):
        
        st.subheader("Methods & Materials")
        
    
        st.markdown("**General workflow of Project 2: GWAS-MNER**  \n\n Below is a simple workflow (Figure 1) depicting how Project 2 was structured in terms of dataset curation, model training and testing, as well as the final user-friendly product.")
        
        st.image('https://raw.githubusercontent.com/nick-mcq/GWAS-MNER/main/workflow.PNG', caption="Figure 1: GWAS-MNER overall workflow. This flowchart highlights the development process of the GWAS-MNER web-tool, from its inception with specially curated publications, to the final product open to all users on this website. Named entity recognition (NER) models were trained and tested on the command-line in Bash, with the final pipelines being deployed in Python 3.8.5. Of the 1200 publications used to create the web-tool, the first 700 papers served as training data, with the remaining 500 used as a unique training set.")
        
        st.markdown("**Dataset Curation & Extraction**  \n\n In order to obtain a working named entity recognition (NER) model, a comprehensive amount of data, with specifically labelled entities for the model to recognise later, is required. This data was obtained through the use of AutoCORPus, which allowed for the automatic curation and extraction of Methods & Materials sections for 1200 PubMed GWAS publications. The resulting output consisted of JSON files which can be further parsed manually.  \n\n Following initial automatic data curation, entities of interest were labelled individually based on pattern recognition using Regular Expressions (RegEx) in Python 3.8.5. These patterns were able to pick up any keywords, in addition to labelling their start and end characters in the analysed string.  \n\n Following these two data collection steps, indicated in Figure 1, the 1200 publications were divided into a training set (composed of the first 700 papers) and a testing set (composed of the remaining 500 papers) to develop the machine learning models.")
        
        st.markdown("**NER “branch models” approach: training & testing models**  \n\n In the given timeframe to complete the project, the most logical approach in developing GWAS-MNER consisted of splitting the tool into 5 relevant branches depending on which entities the user wants to identify. These separate branches are described in Figure 2, highlighting this modular approach to using machine learning in metadata extraction.")
        
        st.image('https://raw.githubusercontent.com/nick-mcq/GWAS-MNER/main/branchmodels.PNG', caption="Figure 2: Schematic illustrating the 5 different branches developed for GWAS-MNER. While all branches were trained and tested using the same datasets, labelled entities vary from model to model, as they were designed to identify different metadata elements, with each branch depicting an example of what it attempts to identify.")
      
        st.markdown("For GWAS-MNER, spaCy 3.0 was chosen to develop the machine learning algorithms. An open-source NLP library accessible through Python, spaCy is known to be remarkably fast and provides some of the most accurate results among similar NLP options (Colic & Rinaldi, 2019). Further, the newest iteration of the library, spaCy 3.0, was released earlier this year, making it the most modern approach to NLP. In terms of model architecture, spaCy uses word embedding and a multilayer convolution neural network (CNN) along with residual connections  (Digan et al., 2021). This CNN allows the user to choose between a more efficient model, a more accurate model, or a balanced version of both. In the case of GWAS-MNER, the default 'en_core_web_lg' python package was installed to pretrain the algorithms, and the models were optimised specifically for accuracy over training & testing speed. Further, maximum batch size was set to 1000 and the proprietary spaCy quickstart configuration file was deployed for every single branch model, allowing for unlimited epochs until the model scoring plateaus.")
      
        st.markdown("**Website Design**  \n\n The chosen third-party application for the development of the website itself is Streamlit, a Python library which can be used to code modifiable elements to form a web-page which can be hosted both locally and through GitHub using streamlit.share. Moreover, Streamlit provides direct compatibility with spaCy through the streamlit.spacy module in Python 3.8, allowing for the direct integration of the visualiser to observe NER results obtained by GWAS-MNER.")
      
        if st.button("Methods Glossary", help = 'Press me to reveal a glossary defining some previously undefined key terms used in this section'):
            st.warning('**spaCy 3.0**: spaCy is an open-source natural language processing software library written in Python and Cython. The latest version available is 3.0. \n\n **NER**: In the context of natural language processing, Named Entity Recognition (NER) is a procedure where plaintext is parsed through to identify entities which can be categorised, such as with names, companies, quantities, software programs, etc... \n\n **RegEx**: A regular expression (RegEx) is a string of special characters which denote a search pattern. This pattern can then be applied tto identify matches in plaintext inputs. \n\n **CNN**: A convolutional neural network (CNN) is a deep learning neural network used for processing complex, structured arrays of information.')
      
        empty=False
        
      if st.sidebar.checkbox("Results"):
        
        st.subheader("Results")
        
        st.markdown('**Final branch models: entities and scoring for each branch output**')
    
        st.markdown("After training and testing is complete, 5 working branches were formed for GWAS-MNER. Each branch and their respective entities for which they identify can be seen in Table 1:")
    
        st.image('https://raw.githubusercontent.com/nick-mcq/GWAS-MNER/main/table.PNG', caption='Table 1: GWAS-MNER branches and entity tags. Each branch is specialised to extract specific entities based on the data it was trained and tested with. Abbreviations: SNP = single nucleotide polymorphism, QC = quality control.')
    
        st.markdown("It should be noted that certain entities, such as ‘negation’ and ‘NO imputation’, were added into branches which may benefit from tracking whether statements alluding to *not* performing an action or task, i.e., “we did *not* perform any quality control measures”. In particular, the 'NO imputation' entity tags words which are specially designed to indicate a lack of imputation in results or a dataset, such as through the terms 'non-imputed' or 'unimputed'. Further, in the software-heavy QC branch, the algorithm was also able to detect version numbers, often helpful in ensuring exact reproducibility.")
    
        st.markdown("Once finished, each model was given a sample text to verify that it functions as expected. Such an example, which also demonstrates the visualising capabilities of spaCy and Streamlit, can be found in Figure 3. ")
    
        st.image('https://raw.githubusercontent.com/nick-mcq/GWAS-MNER/main/example.PNG', caption="Figure 3: Example of spaCy's visualising software. This image captured the format used by spaCy to showcase when the GWAS-MNER model successfully identifies and tags an entity in a sample text. In this case, the QC (quality control) branch was selected for entity recognition.")
    
        st.markdown("Each branch was also scored internally using F1 scoring, as this is the standard scoring method for machine learning algorithms, during the testing phase, allowing for overall comparison of branch quality. These scores helped shape updates and improvements to the datasets used for training, with a perfect score of 1.00. These aforementioned scores can be found in the bar chart below (Figure 4), which can be enlarged and is downloadable in a number of formats.")
    
       
    
        source = pd.DataFrame({
    'Branch Model': ['Platform', 'Total SNPs', 'Assays', 'QC', 'Imputation'],
    'spaCy Score': [1.00, 0.89, 0.82, 0.98, 0.95]
})
    
        chart = alt.Chart(source).mark_bar().encode(
    x=alt.X('Branch Model', type='nominal', sort=None),
    y='spaCy Score'
)
        
        
        text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-13,
    
).encode(
    text='spaCy Score'
).properties(
    title='spaCy F1 scoring of each "best" branch model'
)
    
       
    
        st.altair_chart(chart + text, use_container_width=True)
        
        
        st.image('https://raw.githubusercontent.com/nick-mcq/GWAS-MNER/main/placeholder.PNG', caption="Figure 4: This bar chart displays the F1 scores, calculated using precision and recall of each model, for each individual branch. These scores range from 0.82 to 1.00, depending on the complexity of the branch.")
        
        st.markdown('**Functional web-tool deployment with integrated NER pipelines**')
        
        st.markdown('Despite the importance of the previously discussed results, the true product of this project is most evidently observable through active use of the finalised web-tool. I encourage the reader to consider using the navigational dropdown menu on the left-hand side to switch over to the “NER web-tool” tab, which will redirect to a new page where the different branches are active. Note that a second drop-down menu will also appear: this allows the user to switch between branch models, thereby updating the web-page automatically based on the new selection. Once a branch model has been selected, the first text box which appears (which contains by default a sample piece of text) can be edited, thus allowing the user to enter any text from any publication to be tagged by the NER model. Once confirmed, a visualiser resembling Figure 3 will appear with the results, in addition to a data-frame containing the exact numerical indexes of the tagged entities within the text. Moreover, a ‘DOWNLOAD’ button appears at the bottom of the page, which will download the results of the NER in the working directory of the web-tool in JSON format (in fact, two version are downloaded, the raw JSON file and a trimmed JSON file). It is important to note that currently the working directory of the web-tool requires admin access to be reached (nevertheless, the button has been tested, and is fully functional).')
    
        if st.button("Results Glossary", help = 'Press me to reveal a glossary defining some previously undefined key terms used in this section'):
            st.warning("**F1 score**: In statistical analysis of machine learning models, the F-score represents a model's accuracy. It is calculated from the precision and recall of the model, specifically with the number of true-positives divided by the number of all-positives (thus including false-positives) defined as precision, and the number of true-positive divided by the number of entities that were meant to be identified as positive defined as recall. F1 scoring ranges from 1.0 (perfect) to 0.0 (zero precision or recall). \n\n **PLINK**: PLINK is a free-to-use, open-source analysis software, able to perform a range of simple, large-scale analyses on whole genomes for the purpose of quality control in GWAS data.")
    
        empty=False
    
      if st.sidebar.checkbox("Discussion"):
        
        st.subheader("Discussion")
        
        st.markdown('**Argument for the use of machine-learning based curation in GWAS data**')
    
        st.markdown("Manual curation of GWAS metadata can be considered laborious, particularly when dealing with a large scale of publications, time consuming and subject to individual variability, such that an individual may format their results in a unique manner, whereas machine-driven programs have been trained to produce a single, uniform output which can then be reintegrated into further systems, data analysis or stored in larger centralised databases. In fact, some attempts at automating data curation in GWAS have already been made, with relative success in terms of model predictions (Kuleshov et al., 2019). It is therefore evident that an avenue is presenting itself for the introduction of algorithms in aiding the effort to curate and parse through data obtained from bioscience-related publications. In fact, using the models shown in this report, Platforms (i.e. manufacturers), QC and Imputation can be automatically retrieved with very high accuracy (ranging from 0.95 to 1.00 in F1 scoring, as seen in Figure 4). As a result, a larger open-access database such as GWAS Central (Beck, Shorter & Brookes, 2020) could make great use of the results obtained through GWAS-MNER. Overall, the use of NLP and NER in particular could prove hugely valuable in automatically scraping key data for further work or documentation; the important distinction to be made in the case of this tool is that which data the user requests is customisable, opening up new possibilities in terms of individual user-orientated machine learning-driven results.")
        
        st.markdown('**Limitations in GWAS-MNER: discrepancy in branch scores and size of model outputs**')
        
        st.markdown("The accuracy of a branch can be directly correlated with the complexity of the entity with which a label is associated, as it results in more likely cases of confusion within the algorithm's predetermined Regular Expression parameters, often resulting in data being omitted to prevent fatal errors. However, these are all variables which can be adjusted by the developer, which points towards potential for perfecting, when there is sufficient time to do so. In the context of this project, for example, the Assays branch (Figure 4) presents with a significantly lower score than the Platform branch, at 0.82 compared to 1.00; this discrepancy in scoring is not only due to the data used for training the Assays branch being significantly more complex (in addition to newer, unseen before assays always being developed), but also due to this branch being the last one created in the Project 2 timeline, meaning it had the least time for improvement and quality control. Moreover, a NER tool requires a significant amount of valid training and testing data to accurately label correct entities: it could be argued that much more data is required for a truly high-performance output to be generated. Finally, each model output takes between 700MB and 800MB of storage on any given hard-drive, making it more difficult to deploy a multi-branch NER tool such as GWAS-MNER in a strictly online environment, as loading each branch would require a download of the aforementioned size to be able to run the branch model.")
        
        if st.button("Discussion Glossary", help = 'Press me to reveal a glossary defining some previously undefined key terms used in this section'):
            st.warning("**GWAS Central**: GWAS Central boasts a centralised collection of summary-level results from GWAS publications, both large and small in scale, serving as an open-source repository for all data-scientists in genomics. \n\n **700MB to 800MB**: This is the range of space required in megabytes on the hard-drive of whichever computer is running GWAS-MNER, for EACH branch, meaning that in reality up to 4GB (gigabytes) of hard-drive memory is necessary to run the full web-tool. For reference, the entire application used to host the web-tool and display this report is a mere 37KB (kilobytes) large, or 10 000 fold smaller than 1 branch output.")
        
        empty=False
    
      if st.sidebar.checkbox("Future Work"):
        
        st.subheader("Future Work")
        
    
        st.markdown("Due to the time constraints imposed upon this project, an initially proposed multi-model version of the algorithm was not produced, such that it would combine all branches into one algorithm searching for all entities simultaneously. This combined branch model would be much easier to deploy online and could provide streamlined results, although its accuracy relative to the current separate branch version would need to be benchmarked. Further, the lack of data in regards to Perlegen assays proved detrimental in providing the algorithm with sufficient data for recognising such assays: there is a lack of older publications in the training datasets which cover potentially antiquated assays and platforms such as with Perlegen. Overall, there is room for improvement in the majority of the branch models; expanding the datasets fed into the program would prove valuable in furthering the capabilities of GWAS-MNER. In essence, the short nature of the project did not leave much room for progression, rather a finished version of each branch was prioritised.")
    
        if st.button("Future Work Glossary", help = 'Press me to reveal a glossary defining some previously undefined key terms used in this section'):
            st.warning("**Perlegen**: Perlegen was founded in 2000 with the goal of creating genomic assays to observe genetic variations in the form of identifying common SNPs between experimental subjects. However, this company was eventually acquired by the larger Affymetrix, meaning that its assays have been absorbed and are less likely to appear in modern GWAS publications.")
    
        empty=False
        
      if st.sidebar.checkbox("Conclusion"):
        
        st.subheader("Conclusion")
        
    
        st.markdown("To summarise, this project proposed a machine-learning tool which is capable of identifying and extracting key metadata from GWAS publications in a structured manner, such that the subsequent output can be integrated further downstream. The results are promising, although there is much room for improvement of the branch models showcased in this report; nevertheless, this system opens the door to the world of automated curation of biomedical literature, thereby providing an efficient and organised method of synthesising key methods to the benefit of the user. Finally, it should be mentioned that this web-tool’s design was made possible using the impressive, automated extracting power of AutoCORPus, highlighting GWAS-MNER as a prime example of an NLP-based algorithm which benefitted from its utility. Moreover, this process could be adapted for publications covering other topics, or even multiple topics, based on how much data is available.")
    
        empty=False
    
      if st.sidebar.checkbox("References"):
        
        st.subheader("References")
        
    
        st.markdown("Beck, T., Shorter, T. & Brookes, A.J. (2020) GWAS Central: a comprehensive resource for the discovery and comparison of genotype and phenotype data from genome-wide association studies. Nucleic Acids Research. [Online] 48 (D1), D933–D940. Available from: doi:10.1093/nar/gkz895.  \n\n Beecham, G.W., Martin, E.R., Li, Y.-J., Slifer, M.A., et al. (2009) Genome-wide association study implicates a chromosome 12 risk locus for late-onset Alzheimer disease. American Journal of Human Genetics. [Online] 84 (1), 35–43. Available from: doi:10.1016/j.ajhg.2008.12.008. \n\n Brown, C.C., Havener, T.M., Medina, M.W., Auman, J.T., et al. (2012) A genome-wide association analysis of temozolomide response using lymphoblastoid cell lines reveals a clinically relevant association with MGMT. Pharmacogenetics and genomics. [Online] 22 (11), 796–802. Available from: doi:10.1097/FPC.0b013e3283589c50. \n\n Chang, C.C., Chow, C.C., Tellier, L.C., Vattikuti, S., et al. (2015) Second-generation PLINK: rising to the challenge of larger and richer datasets. GigaScience. [Online] 4. Available from: doi:10.1186/s13742-015-0047-8 [Accessed: 13 June 2021]. \n\n Colic, N. & Rinaldi, F. (2019) Improving spaCy dependency annotation and PoS tagging web service using independent NER services. Genomics & Informatics. [Online] 17 (2). Available from: doi:10.5808/GI.2019.17.2.e21 [Accessed: 8 June 2021].  \n\n Digan, W., Névéol, A., Neuraz, A., Wack, M., et al. (2021) Can reproducibility be improved in clinical natural language processing? A study of 7 clinical NLP suites. Journal of the American Medical Informatics Association: JAMIA. [Online] 28 (3), 504–515. Available from: doi:10.1093/jamia/ocaa261.  \n\n Hu, Y., Sun, S., Rowlands, T., Beck, T., et al. (2021) Auto-CORPus: Automated and Consistent Outputs from Research Publications. bioRxiv. [Online] 2021.01.08.425887. Available from: doi:10.1101/2021.01.08.425887.  \n\n Kuleshov, V., Ding, J., Vo, C., Hancock, B., et al. (2019) A machine-compiled database of genome-wide association studies. Nature Communications. [Online] 10. Available from: doi:10.1038/s41467-019-11026-x [Accessed: 8 June 2021]. \n\n Lee, S., Liang, X., Woods, M., Reiner, A.S., et al. (2020) Machine learning on genome-wide association studies to predict the risk of radiation-associated contralateral breast cancer in the WECARE Study. PLOS ONE. [Online] 15 (2), e0226157. Available from: doi:10.1371/journal.pone.0226157. \n\n Pandey, K.R., Maden, N., Poudel, B., Pradhananga, S., et al. (2012) The Curation of Genetic Variants: Difficulties and Possible Solutions. Genomics, Proteomics & Bioinformatics. [Online] 10 (6), 317–325. Available from: doi:10.1016/j.gpb.2012.06.006. \n\n  Stein, J.L., Medland, S.E., Vasquez, A.A., Hibar, D.P., et al. (2012) Identification of common variants associated with human hippocampal and intracranial volumes. Nature genetics. [Online] 44 (5), 552–561. Available from: doi:10.1038/ng.2250. \n\n Zeggini, E., Scott, L.J., Saxena, R., Voight, B.F., et al. (2008) Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes. Nature genetics. [Online] 40 (5), 638–645. Available from: doi:10.1038/ng.120.")
    
        empty=False
        
      if empty==True:
          
          st.subheader("Abstract")

          link = 'Source code: https://github.com/nick-mcq/GWAS-MNER'
          st.write("""In the context of genome wide association studies (GWAS), reproducibility can prove to be a valuable attribute of the published experiments; this inherently calls for a method to obtain all information necessary to confirm, categorise and potentially reproduce data and results of GWAS. Currently, this curation process is achieved through laborious and time consuming manual identification techniques. New developments in the sphere of machine learning, particularly with natural language processing (NLP) models and algorithms dedicated to data mining and annotating text documents, have presented novel options for the recognition and extraction of key information and metadata from scientific publications. GWAS Metadata Named Entity Recogniser (GWAS-MNER) is the culmination of these advancements; this NLP tool was developed in Python using spaCy 3.0 named entity recognition (NER) as a method for identifying key metadata elements in scientific texts specifically pertinent to GWAS. GWAS-MNER is composed of 5 separate model branches: Platform, Imputation, Total SNPs, Quality Control and Assays. Each branch is able to identify specific metadata elements uniquely, with F1-scores from 0.82-1.00 for the different branches. This report highlights the development and capabilities of GWAS-MNER, a stand-alone web-tool for the extraction of pertinent information from GWAS publications. \n\n Key words: GWAS, Natural Language Processing, Named Entity Recognition, Machine Learning, SNPs""")
          st.markdown(link, unsafe_allow_html=True)
          #st.write('')
          
      
    
    elif choice == "NER web-tool":
      st.subheader("Named Entity Recognition")
      # Add a selectbox to the sidebar:
      sel = st.sidebar.selectbox("Which entity would you like to identify?", ["Platform", "Imputation", 'Total SNPs', 'Quality Control', 'Assays'])
      if sel=="Platform":
         #path=model_loader("https://github.com/fm1320/IC_NLP/releases/download/V3/V3-20210203T001829Z-001.zip", "V3")   
         nlp1 = spacy.load('platform/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","Total RNA from the middle temporal cortex (Brodmann areas 20 and 21) from 86 subjects was isolated and randomly hybridized to Affymetrix Human Exon 1.0 ST arrays, and quality control analysis was performed using standard methods. The effects of several methodological (day of expression hybridization, RNA integrity number (RIN)) and biological covariates (sex, age and medication) on exon–gene expression relationships were tested for significance. Of these individuals, 71 had participated in a published epilepsy genome-wide association study, and, therefore, genotyping data were available. Details of sample collection and genotyping quality control steps have been published previously66. These samples were assayed with Illumina HumanHap550v3 (N = 44) and Illumina Human610-Quadv1 (N = 27) arrays.", help="Sample text source: Stein, J.L., Medland, S.E., Vasquez, A.A., Hibar, D.P., et al. (2012)")   
         docx = nlp1(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp1.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD", help="Press me to download the results in JSON format (note that this currently downloads the files into the working directory of the streamlit app, which requires admin access)"):
             
             
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
         nlp2 = spacy.load('imputation_negation/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","To validate additional associated SNPs (p < 0.0001) and nominally associated candidate genes, we imputed SNPs from our GWAS using a previously published GWAS1 along with both the IMPUTE and BEAGLE programs. In addition another study, which did not impute any further SNPs, served to further validate our results for candidate genes (see Supplementary Table 5) ", help="Sample text source: Beecham, G.W., Martin, E.R., Li, Y.-J., Slifer, M.A., et al. (2009)")   
         docx = nlp2(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp2.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD", help="Press me to download the results in JSON format (note that this currently downloads the files into the working directory of the streamlit app, which requires admin access)"):
             
             
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
         nlp3 = spacy.load('SNP#/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","We based our further analyses on 2,168,847 SNPs that met imputation and genotyping QC criteria across all studies (Methods; Supplementary Methods). We then conducted a series of association analyses to relate the 2.2 million genotyped and/or imputed SNPs with plasma concentrations of HDL cholesterol, LDL cholesterol and triglyceride concentrations. ", help="Sample text source: Zeggini, E., Scott, L.J., Saxena, R., Voight, B.F., et al. (2008)")   
         docx = nlp3(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp3.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD", help="Press me to download the results in JSON format (note that this currently downloads the files into the working directory of the streamlit app, which requires admin access)"):
             
             
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
         nlp4 = spacy.load('QC/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","Quality control of genotype data and genetic association analyses were performed using PLINK v1.07 ().", help="Sample text source: Chang, C.C., Chow, C.C., Tellier, L.C., Vattikuti, S., et al. (2015)")   
         docx = nlp4(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp4.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD", help="Press me to download the results in JSON format (note that this currently downloads the files into the working directory of the streamlit app, which requires admin access)"):
             
             
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
         nlp5 = spacy.load('assay_total/output/model-best') #this will change based on which choice was made
         raw_text = st.text_area("Enter text for entity recognition","The 529 LCLs derived from the CAP cohort were incubated under standardized conditions for 24hr, after which MGMT transcript levels were quantified using the Illumina H8v3 beadarray. Individuals in the WHI-SHARe cohort were genotyped on the Affymetrix 6.0 array.", help="Sample text source: Brown, C.C., Havener, T.M., Medina, M.W., Auman, J.T., et al. (2012)")   
         docx = nlp5(raw_text)
         spacy_streamlit.visualize_ner(docx,labels=nlp5.get_pipe('ner').labels) 
         
         st.write('')
         
         if st.button("DOWNLOAD", help="Press me to download the results in JSON format (note that this currently downloads the files into the working directory of the streamlit app, which requires admin access)"):
             
             
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
      
      
         st.error('***The NLP package used in this web-tool originates from SpaCy 3.0, a very recently developed package which makes use of machine learning efficiently and as accurately as possible; however as the word "learning" implies, the algorithm is not perfect and can mistakingly label entities which may "resemble" those it recognises.*** :nerd_face:')
      
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
