import pandas as pd 
import numpy as np 

X = pd.DataFrame()
X['score'] = np.ones(857)
X['tweet'] = ""

i=0
f = open("anger.txt", "r")
for line in f :
    l = line.split('\t')
    #print float(l[3][:-1])
    #break
    X['tweet'][i] = l[1]
    X['score'][i] = float(l[3][:-1])
    i += 1

X.to_csv('anger.csv', index=False)