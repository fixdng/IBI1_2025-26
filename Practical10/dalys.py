import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/home/ai/IBI1_2025-26/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#In Afghanistan,year 1998 reported the maximum DALYs across the first 10 years
dalys_data.iloc[0:10,2:4]

#in these data, the first year is 1990 and the last year is 2019
dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]

# the countries with the maximum DALYS is Lesotho and with the minimum DALYS is Singapore
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]

#plot
le = dalys_data.loc[dalys_data["Entity"] == "Lesotho"]
plt.plot(le.Year, le.DALYs, 'bo')
plt.xticks(le.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in Lesotho")
plt.show()


#question
question_data = dalys_data.loc[dalys_data["Year"] == 2019, "DALYs"]
plt.hist(question_data, bins=30)
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across all countries in 2019")
plt.show()