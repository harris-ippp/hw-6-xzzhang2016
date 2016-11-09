import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
election=[]
for line in open("ELECTION_ID"):
    a = line.split()
    year = a[0]+".csv"
    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(year, index_col = 0,thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = a[0]
    election.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
combined = pd.concat(election)
combined["Republican Share"]=combined["Republican"]/combined["Total Votes Cast"]
accomack = combined.loc['Accomack County'].sort_values(by = 'Year', ascending = True)
figure = accomack.plot(kind= "line", x ="Year", y="Republican Share")
figure.get_figure().savefig('accomack.png', )
