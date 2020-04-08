#%%[markdown]
# This file looking like this is no coincidence. This script is written in VScode to run interactively. 
# Once the code is ready, it can be interactively run. It is possible to run this whole file as a script as well.
# Using the `Python: Export Current Python File as Jupyter Notebook` on the command palette, 
# this `.py` file can be converted into a jupyter noteobok. 

## Introduction


## Methodology


## Analysis


#%%[code]
# import libraries
import pandas as pd
import sqlite3

# connect to sqlite
with sqlite3.connect("nmc.db") as conn:
    doctors = pd.read_sql("select * from doctors", conn)

print(doctors.describe)

# %%

total_doctors = len(doctors)

print(f'There are {total_doctors} doctors registered through Nepal Medical Council')

# %%

#%%
doctors.groupby(["degree","gender"]).count().reset_index()



# %%
