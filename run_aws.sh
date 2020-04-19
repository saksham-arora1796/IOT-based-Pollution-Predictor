#!/bin/sh

#Run the model on server after every 15 minutes
while :
do
	python3 /home/ubuntu/model.py
	sleep 900
done
