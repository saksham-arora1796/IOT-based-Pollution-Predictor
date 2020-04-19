IOT based Pollution Predictor

System Requirements:

1.	Python Version - 3.7.4
2.	System - 8GB RAM

Hardware Requirements:

1.	Raspberry Pi Module
2.	Connecting wires
3.	Monitor for Pi Module
4.	External keyboard for Pi Module

About the Project:
The project is based on predicting pollution in real time. The project uses Python programming with machine learning techniques (Multiple Linear Regression) to analyze the data reading given by the Raspberry Pi module and visualize it using D3.js library in real time over the website created over EC2 using the Amazon Web Services.

Python Scripts

1.	example.py
This script is responsible for invoking the MQ-135 pollution sensor to start reading the pollution levels of the specified pollutants, namely; Smoke, Carbon Monoxide and LPG. The pollutant data was collected in ppm (parts per million).

2.	mq.py
This script holds the calibrations to the pollution sensor and to the ADC – MCP3008, which is an analog to digital convertor used for converting the sensor analog signals to digital readable data.

3.	MCP3008.py
This script holds the ADC calibrations and also the code needed to call the referencing library SpiDev to work accordingly.
Code: from spidev import SpiDev

Once we have all the readings, we append those reading to a csv file called export.csv which then is send to the Amazon EC2 instance for further analysis. 

4.	Model.py
Now that the export.csv file is on the server we can apply the machine learning techniques over it for the final output.
This process is automated over the instance with a shell script that runs every 15 minutes to dynamically update the reading in real time over the html page created for the final output.

Amazon EC2 Instance

Index.html:
This html page acts as the front end to the project displaying the pollution predictions in real time. The page dynamically changes every 15 minutes with the most updated readings. Hence, notifying any individual of the potential increase in the pollution levels.
