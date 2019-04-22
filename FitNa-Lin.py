import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

path2 = '/Users/rnarang/desktop/research/rdr3/'
pathmoc = '/Users/rnarang/desktop/research/Moc2/'

x = []
y = []
Err=[]
i=0
for fname in os.listdir(path2):
    # i+=1
    # if i == 1000:
    #     break
    if fname == '.DS_Store':
        continue
    elif fname == '.csv.csv.csv':
        continue
    else:
        MocDF = pd.read_csv(pathmoc + 'supermoc2.csv')
        df = pd.read_csv(path2 + fname, delimiter=',')
        print(fname)
        wavelengths = df[['# wave ']]

    MocDF.set_index('File', inplace=True)
    try:
        mocval = MocDF.loc[fname, 'Na2O']
        errval = MocDF.loc[fname, 'Na2O RMSEP']
    except KeyError:
        continue

    dfvis = df[2047:4094]
    vis_total = dfvis[['channel total']].sum()

    dfinfra = df[4095:5860]
    infra_total = dfinfra[['channel total']].sum()

    Nainfra = df[5701:5710]
    Nainfra_bkgd = (df[5698:5569] + df[5713:5714])
    Nainfrasum = float(Nainfra[['channel total']].sum() - ((Nainfra_bkgd[['channel total']].sum())/2))
    Nainfrasum_normalize = float(Nainfrasum / infra_total)
    #
    Na = df[4610:4620]
    Na_bkgd = (df[4607:4608] + df[4622:4623])
    Nasum = float((Na['channel total'].sum()) - ((Na_bkgd['channel total'].sum())/2))
    Nasum_normalize = float(Nasum / infra_total)
    Na_total = Nasum_normalize + Nainfrasum_normalize
    x.append(mocval)
    y.append(Na_total)
    Err.append(errval)

ultarray = (np.array(list(zip(x,y,Err))))
xnew,ynew,Naerr = zip(*ultarray)
xnp = np.array(xnew)
ynp = np.array(ynew)
Naerrnp = np.array(Naerr)

def line_fit(x, a):
    return a*x

fitline, covarline = curve_fit(line_fit, xnp, ynp, sigma=Naerrnp, bounds=(0., 1.0))
A = fitline
plt.plot(np.sort(xnp), line_fit(np.sort(xnp), *fitline), 'k-', label='Linear Fit')
print(fitline)

plt.scatter(x,y,color='red', s=1, label='Data')
plt.title("Both Sodium Peaks vs. Chemcam's weight percentage with Linear Fit")
plt.xlabel('Chemcam wt % for Na')
plt.ylabel('Percent of counts attributed to both Na peaks')
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()

