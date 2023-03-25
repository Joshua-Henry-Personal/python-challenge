# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:42:20 2023

@author: sky_s
"""

# import pandas as pd
import pandas as pd
import datetime  
import os, glob


# path location of the data
filepath = "./Resources/budget_data.csv"
  
parser = lambda date: pd.datetime.strptime(date, '%b-%y')
 
# read the CSV file
df = pd.read_csv(filepath,parse_dates=['Date'],date_parser=parser,dtype = {'Profit/Losses': int})
 

df = df.sort_values('Date', ignore_index=True)

df['LastMth'] = df['Profit/Losses'].shift(1)
df['chg'] = df['Profit/Losses'] - df['LastMth'] 
total_mean = df["chg"].mean()

total_vol = df["Profit/Losses"].sum()

file = "./Resources/export.txt"

f = open(file, "w")


print('Financial Analysis')
print('')
print('----------------------------')
print('')
print('Financial Analysis',file=f)
print('',file=f)
print('----------------------------',file=f)
print('',file=f)

month_count = df["Date"].dt.month.count()
print('Total Months: ', + month_count)
print('Total Months: ', + month_count,file=f)

print('Total: $', + total_vol)
print('Total: $', + total_vol,file=f)

print('Average Change: $', format(total_mean, '.2f'))
print('Average Change: $', format(total_mean, '.2f'),file=f)


date_max = df.loc[df["chg"] ==  df["chg"].max(), ['Date','chg']]
date_max['chg'] = df['chg'].apply('${:.0f}'.format)
date_max['Year_Month'] = df['Date'].dt.strftime('%b-%y')
print('Greatest Increase in Profits: '+date_max['Year_Month'].to_string(index=False)+" ("+date_max['chg'].to_string(index=False)+')')
print('Greatest Increase in Profits: '+date_max['Year_Month'].to_string(index=False)+" ("+date_max['chg'].to_string(index=False)+')',file=f)


date_min = df.loc[df["chg"] ==  df["chg"].min(), ['Date','chg']]
date_min['chg'] = df['chg'].apply('${:.0f}'.format)
date_min['Year_Month'] = df['Date'].dt.strftime('%b-%y')
print('Greatest Decrease in Profits: '+date_min['Year_Month'].to_string(index=False)+" ("+date_min['chg'].to_string(index=False)+')')
print('Greatest Decrease in Profits: '+date_min['Year_Month'].to_string(index=False)+" ("+date_min['chg'].to_string(index=False)+')',file=f)




f.close()

