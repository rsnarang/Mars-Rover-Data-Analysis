import os
for filename in os.listdir('/Users/[user]/desktop/research/CCdata/'):
    if filename.endswith('.lbl'):
        os.remove(os.path.join('/Users/[user]/desktop/research/CCdata/',filename))
