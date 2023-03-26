# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:42:20 2023

@author: sky_s
"""

# import pandas as pd
import pandas as pd
import datetime  
import sys


# path location of the data
filepath = ".\Resources\election_data.csv"
  
 
# read the CSV file
df = pd.read_csv(filepath)

df['Counter'] = 1


file = ".\Resources\export.txt"

df['counter_pct'] = (df['Counter'] / 
                  df['Counter'].sum()) * 100

cand_count = df["Ballot ID"].count()

dftal = df[["Candidate","counter_pct","Counter",]]
cand_tally = dftal.groupby('Candidate').sum()
cand_tally.reset_index(inplace = True, drop = False)
cand_max = cand_tally.loc[cand_tally["counter_pct"] ==  cand_tally["counter_pct"].max(), ['Candidate']]
cand_tally['counter_pct'] = cand_tally['counter_pct'].apply('{:.3f}%'.format)


print('Election Results')
print('')
print('----------------------------')
print('')
print('Total Votes: ', + cand_count)
print('')
print('----------------------------')
print(cand_tally.to_string(header=False,index=False))
print('')
print('----------------------------')
print('')
print('Winner  '+(cand_max.to_string(header=False,index=False)))
print('')
print('----------------------------')

f = open(file, "w")
print('Election Results',file=f)
print('',file=f)
print('----------------------------',file=f)
print('',file=f)
print('Total Votes: ', + cand_count,file=f)
print('',file=f)
print('----------------------------',file=f)
print(cand_tally.to_string(header=False,index=False),file=f)
print('',file=f)
print('----------------------------',file=f)
print('',file=f)
print('Winner  '+(cand_max.to_string(header=False,index=False)),file=f)
print('')
print('----------------------------',file=f)
f.close()

