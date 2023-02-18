import pandas as pd
import numpy as np

data = pd.read_csv('final.csv')

data['Price'] = data['Price'].apply(lambda x: x.split('€')[0])
data['Email_count'] = data['Email_count'].apply(lambda x: x.split()[0])

data.to_csv('Final.csv',index=False)