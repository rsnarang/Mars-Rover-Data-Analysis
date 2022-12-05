import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#paths obviously
path2 = '/Users/[user]/desktop/research/rdr3/'
pathmoc = '/Users/[user]/desktop/research/Moc2/'

#initializing my lists
x=[]
y=[]
i = 1
#loop to read moc file and every csv file
for fname in os.listdir(path2):
    # i += 1
    # if i == 50:
    #     break
    if fname == '.DS_Store':
        continue
    elif fname == '.csv.csv.csv':
        continue
    else:
        MocDF = pd.read_csv(pathmoc + 'supermoc.csv')
        df = pd.read_csv(path2 + fname, delimiter=',')
        print(fname)
        wavelengths = df[['# wave ']]

    MocDF.set_index('File', inplace=True)
    try:
        mocval = MocDF.loc[fname, 'K2O']
    except KeyError:
        continue

    # infrared region
    dfinfra = df[4097:5850]
    # sum of the entire infrared region
    infra_total = dfinfra[['channel total']].sum()
    # potassium, K background
    K1 = df[5446:5450]
    K1_bkgd = (df[5444:5445] + df[5453:5454])
    K1sum = float(K1[['channel total']].sum()-((K1_bkgd[['channel total']].sum())/2))
    # normalize by dividing the infrared's total region from the K peak
    K1sum_normalize = float(K1sum / infra_total)

    # same as above
    K2 = df[5463:5466]
    K2_bkgd = (df[5460:5461] + df[5468:5469])
    K2sum = float(K2[['channel total']].sum()-((K2_bkgd[['channel total']].sum())/2))
    K2sum_normalize = float(K2sum / infra_total)

    # add both 'normalized' peaks
    Ksum = K2sum_normalize + K1sum_normalize
    # create my x and y axis
    y.append(Ksum)
    # x axis is the moc value corresponding to the file
    x.append(mocval)

ultarray = (np.array(list(zip(x,y))))

xnew,ynew = zip(*ultarray)
xnp = np.array(xnew)
ynp = np.array(ynew)

def log_fit(x, a, b, c):
    return a*np.log(b*x + c)

def line_fit(x, a, b):
    return a*x + b

def sqrt_fit(x, a, b, c):
    return a*np.sqrt(x+b) + c

fitting_parameters, covariance = curve_fit(log_fit, xnp, ynp)
a, b, c = fitting_parameters
plt.plot(np.sort(xnp), log_fit(np.sort(xnp), *fitting_parameters), 'b-', label='Log Fit')
print(fitting_parameters)

# fitline, covarline = curve_fit(line_fit, xnp, ynp)
# A, B = fitline
# plt.plot(np.sort(xnp), line_fit(np.sort(xnp), *fitline), 'k-', label='Linear Fit')
# print(fitline)

# fitsqrt, covarsqrt = curve_fit(sqrt_fit, xnp, ynp)
# C, D, E = fitsqrt
# plt.plot(np.sort(xnp), sqrt_fit(np.sort(xnp), *fitsqrt), 'g-', label='Square Root Fit')
# print(fitsqrt)

plt.scatter(x,y,color='red', s=1, label='Data')
plt.title("2 Potassiums vs. Chemcam's weight percentage with Log Fit")
plt.xlabel('Chemcam wt % for K')
plt.ylabel('Percent of counts attributed to both K peaks')
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
