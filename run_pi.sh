#!/bin/sh

#Running the python script
python /home/pi/run.py

#Uploading the data file to AWS EC2
while :
do
	scp -i /home/pi/Keys/newkey.pem /home/pi/DailyPolLog/export.csv ubuntu@ip:~/DailyPolLog/
	sleep 900
done
