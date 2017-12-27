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

def readTxt(filename):
    count = 0
    dbn = []
    school_dist = []
    school_borough = []
    school_name = []
    numb_taken = []
    reading_score = []
    math_score = []
    writing_score = []
    with open(filename, 'r') as f:
        for line in f:
            content = line.split(",")
            dbn_val = content[0]
            if count > 0:
                dbn.append(str(dbn_val))
                school_dist.append(dbn_val[:2])
                school_borough.append(dbn_val[2:3])
                school_name.append(content[1])
                numb_taken.append(content[2])
                reading_score.append(content[3])
                math_score.append(content[4])
                writing_score.append(content[5])

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
    plotDistricts(districts)
    return dbn, school_dist, school_borough, school_name, numb_taken, reading_score, math_score, writing_score

def plotDistricts(districts):
    print ("Creating bargraph for district frequency--")

    plt.figure(figsize=(20, 10))  # width:20, height:3
    plt.bar(range(len(districts)), districts.values(), align='center', width=0.3)
    plt.xticks(range(len(districts)), list(districts.keys()))
    plt.xlabel("District")
    plt.ylabel("Frequency")
    plt.title("Districts")
    plt.savefig("districts.png")


if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/2012_SAT_Results.csv"
    school_dbn, district_vals, boroughs, names, taken, read, math, write = readTxt(filename)
    # validating list lengths
    print len(school_dbn)
    print len(district_vals)
    print len(boroughs)
    print len(read)
    print len(math)
    print len(write)
"""
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
"""


#print school_borough



#print dbn
        
        #labels.append(content[0])

        #content.pop(0)

        # If we wanted pure lists, and convert from string to float
        #content = [float(elem) for elem in content]
        #content = map(float, content)

        # If we want a list of numpy arrays, not necessary
        #npa = np.asarray(content, dtype=np.float64)

        #examples.append(content)