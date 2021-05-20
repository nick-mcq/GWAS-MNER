#!/bin/sh

cd /project/home20/nam220/NER/AutoCORPus/ #I tell the script to position itself inside the directory which contains the run_app.py for AutoCORPus

echo "Starting at "`date` > extracter_runtime.log #echo = print, it keeps track of when the script starts running
echo "Starting directory is "$PWD >> extracter_runtime.log #prints the directory it runs in to confirm that the above command worked

module load python/3.7.4 #this is the optimal version of pythong according to Cheng (MAKE SURE THAT WHEREVER YOU RUN THIS FROM HAS ACCESS TO THIS VERSION OF PYTHON, if not you need to modify this appropriately

for i in /project/home20/nam220/NER/DATA_RAW/DEV_SET/* #I have included a screenshot of what this folder looks like, this line is iterating through the folders of 100 files each

do #in bash, for loops are in the format "for, do, done"

echo "Running through Folder" $i >> extracter_runtime.log #this is tracking that the correct folders are being iterated through
for n in $i/* #This iterates through each file in each folder in the DEV_SET

do

echo "Processing"$n >> extracter_runtime.log #checks that the correct file is being processed

python run_app.py -f $n -t /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/ -c configs/config_pmc.json
    
    #this line is what you do to run AutoCORPus properly: python run_app.py -f [input file path] -t [output file path] -c [config file]
    #Note: my output file path is "temporary" in that the maintext.json file for each PMC article is extracted from the maintext folder created by AutoCORPus.
    #You would likely have to make the output path dynamic, based on which file you are iterating through
    
rm -r /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/abbreviations #I removed the abbreviations folder, you should probably not do this
rm -r /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/tables #I removed the tables folder, you should probably not do this
mv /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/maintext/* /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/DEV_MAINTEXT #this file moves the maintext content to where I need it, note the usage of * throughout to basically indicate "whatever is inside the folder". If I wanted only files starting with PMC I would do PMC* or if I only wanted json files I would do *.json
rm -r /project/home20/nam220/NER/AUTOCORPUS_EXTRACT/maintext #once I grabbed the maintext.json file, I then deleted the old directory

#PLEASE NOTE: using rm -r is VERY DANGEROUS if you are not sure about what you are deleting, this is a recursive delete tool that is able to wipe out whole directories, so don't use it unless you are CERTAIN about what you wish to delete!

echo "Superfluous files removed, maintext moved to correct directory for "$n >> extracter_runtime.log #this was a line I would use to confirm that the removal of other files and moving process worked

done
done

echo "finished at "`date` >> extracter_runtime.log #noted down the stop date of the script in my runtime.log file

#This script, if you run it with "nohup", will produce a .log file tracking what happened, and will produce a nohup error.log file, in addition to whatever files AutoCORPus should produce
#The following line should be used in the command line to run this script: nohup ./extracter.sh > extracter2_errors_log.out 2>&1 &
# "nohup" stands for no hangup, such that once you run this, it will run the job in the background and you can exit out the server. If you want to check if your script is running, just type in "top" without the quotations, and it'll open up a list of all the processes running on the server. Your process should appear in bold, with a unique process ID (PID). If you find that your process is running or you decide you don't want it to run anymore, type in the following: kill -9 PID (naturally you replace the PID with the number identifying your process)
    
