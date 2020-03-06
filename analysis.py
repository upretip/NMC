#%%[markdown]

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

#%%
doctors.groupby(["gender", "degree"]).count(
    
).pivot_table()



# %%
