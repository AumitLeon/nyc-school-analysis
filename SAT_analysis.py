# Analyzing SAT scores 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
#import keras
#from keras.models import Sequential 
#from keras.layers import Dense
#from keras.layers import Flatten
import numpy as np
#from sklearn import preprocessing
#from keras import regularizers
#from keras.utils import np_utils, generic_utils


#Unique DBN
count = 0
dbn = []
filename = "/mnt/c/Users/Aumit/Documents/2012_SAT_Results.csv"
with open(filename, 'r') as f:
    for line in f:
        content = line.split(",")
        dbn_val = content[0]
        if count > 0:
            dbn.append(str(dbn_val))

            """if str(dbn_val) in dbn:
                dbn[str(dbn_val)] += 1
            else:
                dbn[str(dbn_val)] = 0"""
        count += 1

districts = {}
dist_hist = []
for item in dbn:
    dist = item[:2]
    dist_hist.append(dist)
    if dist in districts:
        districts[dist] += 1
    else:
        districts[dist] = 0

dist_counts = []
for elem in districts:
    dist_counts.append(districts[elem])
print districts
print ("Creating bargraph for district frequency--")

plt.figure(figsize=(20, 10))  # width:20, height:3
plt.bar(range(len(districts)), districts.values(), align='center', width=0.3)
plt.xticks(range(len(districts)), list(districts.keys()))
plt.xlabel("District")
plt.ylabel("Frequency")
plt.title("Districts")
plt.savefig("districts.png")



#print dbn
        
        #labels.append(content[0])

        #content.pop(0)

        # If we wanted pure lists, and convert from string to float
        #content = [float(elem) for elem in content]
        #content = map(float, content)

        # If we want a list of numpy arrays, not necessary
        #npa = np.asarray(content, dtype=np.float64)

        #examples.append(content)