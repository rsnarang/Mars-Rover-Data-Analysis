import os
import pandas as pd


path = '/Users/rnarang/desktop/research/CCdata/'
path2 = '/Users/rnarang/desktop/research/rdr2/'


for fname in os.listdir(path):
    df = pd.read_csv(path+fname, delimiter=',')
    df = df.iloc[15:]
    try:
        newhead = df.iloc[0]
        df.columns = newhead
        df = df.drop([' shot1 ', ' shot2 ', ' shot3 ', ' shot4 ', ' shot5 ', ' mean', ' median'], axis=1)
        df = df.iloc[1:]
    except: IndexError
    df.to_csv(os.path.join(path2, fname))
