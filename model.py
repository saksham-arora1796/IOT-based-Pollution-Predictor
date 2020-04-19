import pandas as pd
from sklearn.linear_model import LinearRegression

try:
	data = pd.read_csv("DailyPolLog/export.csv")
	plot_cut = data.tail(30)
	i=1
except:
	with open("DailyPolLog/Error.log", "a") as fl:
		fl.write("Error Reading File!")

try:
	lreg = LinearRegression().fit(data[['CO', 'Smoke']], data['LPG'])
	creg = LinearRegression().fit(data[['LPG', 'Smoke']], data['CO'])
	sreg = LinearRegression().fit(data[['LPG', 'CO']], data['Smoke'])
	x = []
	for coeff in lreg.coef_:
		x.append(coeff)
	x.append(lreg.intercept_)
	for coeff in creg.coef_:
		x.append(coeff)
	x.append(creg.intercept_)
	for coeff in sreg.coef_:
		x.append(coeff)
	x.append(sreg.intercept_)
	with open("/var/www/html/data/model_output.js", "w") as new:
		new.write("var coef="+str(x)+";")
except:
	with open("DailyPolLog/Error.log", "a") as fl:
		fl.write("Error Working with ML Model!")

try:
	fhand = open("/var/www/html/data/plot.csv", "w")
	fhand.write("date,lpg,co,smoke\n")
	for index, row in plot_cut.iterrows():
			fhand.write(str(i)+","+str(row['LPG'])+","+str(row['CO'])+","+str(row['Smoke'])+"\n")
			i=i+1
	fhand.close()
except:
	with open("DailyPolLog/Error.log", "a") as fl:
		fl.write("Error Storing Plotting Values!")
