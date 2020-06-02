# %%[markdown]
# This file is created so that it can be run interactively using vscode or pycharm.
# It is possible to run this whole file as a script as well.
# Using the `Python: Export Current Python File as Jupyter Notebook` on the command palette, 
# this `.py` file can be converted into a jupyter noteobok. 

## Introduction


## Methodology

# Data was scraped from [NMC](nmc.org.np) website using python (request, beautifulsoup).
# Then it was added to a sqlite database. The insert technique used  `concurrent.futures`
# for multithreading (to parallelize the write to the database).

# This analysis is written on a notebook style interactive document. 
# It uses pandas for data manupulation and plotting

## Analysis
# Men outnumber women in medical profession in Nepal. If divided between different practices (degrees), 
# except for  BDS, the dental professionals, women outnumber men.  
# In MBBS, a general practice doctor, and MD, specialized practice, men outnumber 
# more than 2:1 

# Almost a third (7k+) of the total doctors call Kathmandu Valley (Kathmandu, Bhaktapur, Lalitpur)
# About 118 of them did not have a location listed whereas another 117 or so 
# did not have district name listed (abbreviated, house number, city/locality, etc.)



# %%[code]
# import libraries
import pandas as pd
import sqlite3

# connect to sqlite
from numpy import int64

with sqlite3.connect("nmc.db") as conn:
    doctors = pd.read_sql("select * from doctors", conn)

# %%

total_doctors = len(doctors)

print(f'There are {total_doctors} doctors registered through Nepal Medical Council')

# %%

# first 5 rows of data
print(doctors.head())

# dimension of the dataframe
print(doctors.shape)

# describes the summary statistics of numeric columms
print(doctors.describe())

# column names in the dataframe
print(doctors.columns)

# data type in each columns
print(doctors.dtypes)

# %%
doctors.describe(include=[object])

# %%

# Nepal recognizes third gender

print(doctors.gender.value_counts())
print(doctors['degree'].value_counts())

# %%
doctors.set_index('nmc_number', inplace=True)
# %%
# plotting
doctors.groupby(['gender',"degree"])['gender'].count().unstack(0).plot(kind='bar')
# %%[markdown]

# Additional ideas for analysis
# - Location based analysis. What locations they come from 
#   - we can take out the districts maybe?
# - Name based analysis
#   - Frequent first names
#   - Frequent last names
#   - Match last name with caste/ ethnicity, etc?

# %%
# location based analysis

clean = lambda x: str(x).strip(',. \n\t').replace(" ","").lower().split()

doctors['district'] = doctors['location'].\
    apply(lambda x: x.strip(',.!? \n\t').lower().split(',')[-1].strip())

# %%
# counts = pd.DataFrame(doctors['location'].\
#     apply(lambda x: x.strip(',.!? \n\t').lower().split(',')[-1].strip()).\
#         value_counts())
