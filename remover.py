import os
for filename in os.listdir('/Users/rnarang/desktop/research/CCdata/'):
    if filename.endswith('.lbl'):
        os.remove(os.path.join('/Users/rnarang/desktop/research/CCdata/',filename))