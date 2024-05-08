import pandas as pd
import matplotlib.pyplot as plt
import math

file = pd.read_csv("data/EVV_Weather_Obs_2.csv",header=1)

file["PRCP"]=file["PRCP"].replace(-9999,math.nan)
#drop all nans
file.dropna(subset=['PRCP'],inplace=True)

plt.plot(file['DATE'],file['PRCP'])
plt.ylabel("Average Precepitation")
plt.xlabel("Date")
plt.title("Average Precepitation over time")
plt.show()