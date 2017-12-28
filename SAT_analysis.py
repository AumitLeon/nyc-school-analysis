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
import pandas as pd
from collections import Counter

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
    no_data = False

    with open(filename, 'r') as f:
        df = pd.read_csv(filename)
        temp_names = df['SCHOOL NAME'].tolist()
        for k in range(len(temp_names)):
            if ',' in temp_names[k]:
                temp_name = temp_names[k].split(',')
                final_name = ""
                for seg in temp_name:
                    final_name += seg
                temp_names[k] = final_name
                #print temp_names[k]
        school_name = temp_names
        numb_taken = df['Num of SAT Test Takers'].tolist()
        reading_score = df['SAT Critical Reading Avg. Score'].tolist()
        math_score = df['SAT Math Avg. Score'].tolist()
        writing_score = df['SAT Writing Avg. Score'].tolist()
        dbn = df['DBN'].tolist()

        
        print len(numb_taken)
        print len(writing_score)
        print len(math_score)
        print len(reading_score)

        for g,r,e,p,q in zip(reading_score, math_score, writing_score, numb_taken, dbn):
           # print g
            if g == 's' or r == 's' or e == 's' or p == 's':
                #print "lol"
                reading_score.remove(g)
                math_score.remove(r)
                writing_score.remove(e)
                numb_taken.remove(p)
                dbn.remove(q)
        
        for value in dbn:
            school_dist.append(value[:2])
            school_borough.append(value[2:3])
                
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

def calculateAverages(dbn, dist, borough, name, taken, read, math, write):
    avgScores = {}
    temp_counter = 0
    counts = Counter(dist)
    #print counts['02']
   
    """temp_dist = ""
    for i, sat_math, sat_reading, sat_writing in zip(dist, math, read, write):
        if i not in avgScores:
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            avgScores[i] = float(sat_math) + float(sat_reading) + float(sat_writing)
            #print i
            temp_counter += 1
        else:  
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            #print i
            #print avgScores[i]
            avgScores[i] += float(sat_math) + float(sat_reading) + float(sat_writing)
    
            temp_counter += 1

        if (temp_dist != i and temp_dist != ""):
            #print i
            #print temp_counter
            print avgScores[temp_dist]
            avgScores[temp_dist] = avgScores[temp_dist] / counts[temp_dist]
            #print avgScores[temp_dist]
            print temp_dist
            print counts[temp_dist]
           # print i
            print
        elif i == dist[len(dist)-1]:
            print avgScores[i]
            avgScores[i] = avgScores[i] / counts[i]
            print i
            print counts[i]
            #print
            #print
           # print temp_counter
            #temp_counter = 0
        #elif dist.index(i) == 421:
         #   print "lol"""

    temp_dist = 0
    for i in range(len(dist)):
        if dist[i] not in avgScores:
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            avgScores[dist[i]] = float(math[i]) + float(read[i]) + float(write[i])
            #print i
            temp_counter += 1
        else:  
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            #print i
            #print avgScores[i]
            avgScores[dist[i]] += float(math[i]) + float(read[i]) + float(write[i])
    
            temp_counter += 1

        if (dist[temp_dist] != dist[i] and temp_dist != 0):
            #print i
            #print temp_counter
            #print avgScores[dist[temp_dist]]
            avgScores[dist[temp_dist]] = avgScores[dist[temp_dist]] / counts[dist[temp_dist]]
            #print avgScores[temp_dist]
            #print temp_dist
            #print counts[dist[temp_dist]]
           # print i
            #print
        elif i == len(dist)-1:
            #print avgScores[dist[i]]
            avgScores[dist[i]] = avgScores[dist[i]] / counts[dist[i]]
            #print i
            #print counts[dist[i]]
            #print
            #print
           # print temp_counter
            #temp_counter = 0
        #elif dist.index(i) == 421:
         #   print "lol"



        temp_dist = i
    #print avgScores
    return avgScores

def printScores(dbn, dist, borough, name, taken, read, math, write):
    print "NAME -- READING -- MATH -- WRITE"
    for x in range(len(dbn)):
        print name[x] + " -- " + read[x] + " -- " + math[x] + " -- " + write[x]

def scoresByDist(scores):
    for item in scores:
        print str(item) + " ------ " + str(scores[item])

if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/2012_SAT_Results.csv"
    school_dbn, district_vals, boroughs, names, taken, read, math, write = readTxt(filename)
    #print district_vals
    # validating list lengths
    #print len(school_dbn)
    #print len(district_vals)
    #print len(boroughs)
    #print len(read)
    #print len(math)
    #print len(write)
    scores = calculateAverages(school_dbn, district_vals, boroughs, names, taken, read, math, write)
    scoresByDist(scores)

    #printScores(school_dbn, district_vals, boroughs, names, taken, read, math, write)
