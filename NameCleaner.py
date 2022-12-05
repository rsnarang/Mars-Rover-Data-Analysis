import os
from os.path import join
# import glob

path = '/Users/[user]/desktop/research/rdr2'
for fname in os.listdir(path):
    dst = str(fname[4:12]) + '.csv'
    src = fname
    os.rename(join(path, src), join(path, dst))

# flist = glob.glob('/rdr/*.csv')
# print(flist)


