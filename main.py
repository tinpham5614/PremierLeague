# Import necessary modules
import pandas as pd
import scipy.stats as st

off_int = int(input())

# Read csv file spi_global_rankings.csv into data frame
soccer = pd.read_csv('spi_global_rankings.csv')
# Take the subset of the data where league = "Barclays Premier League"
prem = soccer[soccer["league"] == "Barclays Premier League"] #Code to take subset
print(prem)
#Find mean offensive premier league

mean = prem['off'].mean()
print("Offensive mean of premier league team are:",mean)


# Find total number in subset
n1 = prem['league'].count()# Code to count number in subset

# Find number in subset where off > off_int
x1 = (prem[['off']] > off_int).values.sum()# Code to count number where off > off_int
# print how many teams has more than 2 points of offense
print(x1, 'teams have more than 2.0 points of offensive.')
# Calculate proportion
p1 = x1/n1 * 1.0 # Code to calculate proportion 
print("Sample proportion is", p1)

# Calculate standard error
stderr = (p1 *(1 - p1)/n1) ** 0.5 # Code to calculate standard error

# Find 90% confidence interval
conf_int = (st.norm.interval(0.90, p1, stderr)) # Code to find confidence interval
print(conf_int)

# Find proportion for full data
n2 = len(soccer) # Code to count number in data set
x2 = (soccer[['off']] > off_int).values.sum() # Code to count number in full data set where Age > age
p2 = x2/n2 * 1.0 # Code to calculate proportion

# Determine if the actual proportion falls within the 90% confidence interval
if conf_int[0] <= p2 <= conf_int[1]:
    print("Actual proportion,", p2,", is within the 90% confidence interval")
else:
   print("Actual proportion,",p2 ,", is not within the 90% confidence interval")


my_fav = soccer[soccer["name"] == "Arsenal"]
print(my_fav)