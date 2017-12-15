import pandas as pd 
import numpy as np 

X = pd.read_csv('joy-lexicon.csv')

Y = np.array(X['score'])
del X['score']
np.save('labels.npy', Y)
np.save('lexicon.npy', X.as_matrix())
print X.as_matrix().shape
