import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


path2 = '/Users/rnarang/desktop/research/rdr3/'
pathmoc = '/Users/rnarang/desktop/research/Moc2/'

x=[]
y=[]

for fname in os.listdir(path2):
    if fname == '.DS_Store':
        continue
    elif fname == '.csv.csv.csv':
        continue
    else:
        MocDF = pd.read_csv(pathmoc + 'supermoc.csv')
        df = pd.read_csv(path2 + fname, delimiter=',')
        print(fname)
        wavelengths = df[['# wave ']]

    dfinfra = df[5335:]
    infra_total = dfinfra[['channel total']].sum()

    K1 = df[5464:5469]
    K1_bkgd = (df[5462:5463] + df[5470:5471]) / 2
    K1sum = float(((K1[['channel total']].sum())-K1_bkgd['channel total'].sum())/infra_total)

    K2 = df[5480:5484]
    K2_bkgd = (df[5478:5479] + df[5485:5486]) / 2
    K2sum = float(((K2[['channel total']].sum())-K2_bkgd['channel total'].sum())/infra_total)

    Ksum = K1sum + K2sum
    y.append(Ksum)
    MocDF.set_index('File', inplace=True)
    mocval = MocDF.loc[fname, 'K2O']
    x.append(mocval)

# print(np.array([[d, c] for d, c in zip(x, y)]))

plt.scatter(x,y,color='red')
plt.title("Potassium Peak vs. Chemcam's weight percentage")
plt.xlabel('Chemcam wt % for K')
plt.ylabel('Percent of counts in spectrum attributed to K Peaks')
plt.show()
