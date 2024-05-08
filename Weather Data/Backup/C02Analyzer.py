import pandas as pd
import matplotlib.pyplot as plt
import math

#csv = comma seperated value
#tsv = tab seperated value
#txt = text file
#xlsx = Excel file
file = pd.read_csv("data/co2_data.csv",header=5)



############### Clean The Data Section #############
#remove -99.99 -> going to tell the pandas that it is not a real number
#replaces the -99.99 with nan
file["Average"]=file["Average"].replace(-99.99,math.nan)
#drop all nans
file.dropna(subset=['Average'],inplace=True)


############### Analyze The Data Section #############


############### Visualize The Data Section #############





#print our line graph
#plot(x axis data, y axis date)
plt.plot(file['decimal_year'],file['Average'])
plt.ylabel("Average C02")
plt.xlabel("Years")
plt.title("Average C02 over time")
plt.show()