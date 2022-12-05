import pandas as pd
import glob
flist = (glob.glob('Moc/*.csv'))
pathmoc = '/Users/[user]/desktop/Python/Moc/'
col_list = ['File', 'K2O', 'K2O RMSEP']

df = pd.read_csv(pathmoc + 'UltMocFin.csv')
df2 = df[col_list]

print(df2)
