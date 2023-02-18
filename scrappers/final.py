import pandas as pd
import numpy as np

csvs = ['department.csv','region.csv','Activity.csv','Workforce.csv','Categories.csv','Form.csv','nature.csv','turnover.csv','years.csv']

data =[]
for csv in csvs:
    x = pd.read_csv(csv)
    data.append(x)

data = pd.concat(data)

data.to_csv('final.csv',index=False)
    