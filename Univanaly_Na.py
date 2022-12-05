import os
import pandas as pd
import matplotlib.pyplot as plt

path2 = '/Users/[user]/desktop/research/rdr3/'
pathmoc = '/Users/[user]/desktop/research/Moc2/'

x = []
y = []

for fname in os.listdir(path2):
    if len(x) == 200:
        break
    if fname == '.DS_Store':
        continue
    elif fname == '.csv.csv.csv':
        continue
    else:
        MocDF = pd.read_csv(pathmoc + 'supermoc.csv')
        df = pd.read_csv(path2 + fname, delimiter=',')
        print(fname)
        wavelengths = df[['# wave ']]

    dfvis = df[2049:5335]
    vis_total = dfvis[['channel total']].sum()

    dfinfra = df[5335:]
    infra_total = dfinfra[['channel total']].sum()

    Nainfra = df[5701:5712]
    Nainfra_bkgd = (df[5699:5700] + df[5713:5714]) / 2
    Nainfrasum = float(Nainfra[['channel total']].sum() - Nainfra_bkgd['channel total'].sum())
    Nainfrasum_normalize = float(Nainfrasum / infra_total)

    Na = df[4612:4621]
    Na_bkgd = (df[4610:4611] + df[4622:4623]) / 2
    Nasum = float((Na['channel total'].sum()) - Na_bkgd['channel total'].sum())
    Nasum_normalize = float((Nasum/vis_total))

    Na_total = Nasum_normalize + Nainfrasum_normalize

    MocDF.set_index('File', inplace=True)
    try:
        mocval = MocDF.loc[fname, 'Na2O']
    except KeyError:
        continue
    x.append(mocval)
    y.append(Na_total)

plt.scatter(x,y,color='red')
plt.title("Sodium Peak vs. Chemcam's weight percentage")
plt.xlabel('Chemcam wt % for Na')
plt.ylabel('Percent of counts in spectrum attributed to Na Peaks')
# plt.axis([0, 8, 0, 0.03])
plt.grid(True)
plt.show()
