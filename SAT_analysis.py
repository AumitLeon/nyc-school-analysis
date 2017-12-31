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
import collections

# Extract data from the CSV file
# Extracts data into multiple lists, each of the same length
# Mapping between lists is maintained by index
# i.e, every index maintains corresponds to a particular data point
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

# Plot a bargraph of the distribution of districts
def plotDistricts(districts):
    print ("Creating bargraph for district frequency--")

    plt.figure(figsize=(20, 10))  # width:20, height:3
    plt.bar(range(len(districts)), districts.values(), align='center', width=0.3)
    plt.xticks(range(len(districts)), list(districts.keys()))
    plt.xlabel("District")
    plt.ylabel("Frequency")
    plt.title("Districts")
    plt.savefig("districts.png")

# Calculate average scores by distrcit
def calculateAverages(dbn, dist, borough, name, taken, read, math, write):
    avgScores = {}
    avgMath = {}
    avgReading = {}
    avgWriting = {}
    totTaken = {}
    temp_counter = 0
    counts = Counter(dist)

    temp_dist = 0
    
    # Loop through the lists in parallel
    for i in range(len(dist)):

        # If a district hasn't been encountered yet
        if dist[i] not in avgScores:
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            avgScores[dist[i]] = int(math[i]) + int(read[i]) + int(write[i])
            avgMath[dist[i]] = int(math[i])
            avgReading[dist[i]] = int(read[i])
            avgWriting[dist[i]] = int(write[i])
            totTaken[dist[i]] = int(taken[i])
            #print i
            temp_counter += 1

        # If a district has been encountered already
        else:  
            #print i + " -- " + sat_reading + " -- " + sat_math + " -- " + sat_writing
            #print i
            #print avgScores[i]
            avgScores[dist[i]] += int(math[i]) + int(read[i]) + int(write[i])
            avgMath[dist[i]] += int(math[i])
            avgReading[dist[i]] += int(read[i])
            avgWriting[dist[i]] += int(write[i])
            totTaken[dist[i]] += int(taken[i])
            temp_counter += 1
        
        # Calculate the average if it's the last school in a particular distrcit
        if (dist[temp_dist] != dist[i] and temp_dist != 0):
            #print i
            #print temp_counter
            #print avgScores[dist[temp_dist]]
            avgScores[dist[temp_dist]] = avgScores[dist[temp_dist]] / counts[dist[temp_dist]]
            avgMath[dist[temp_dist]] = avgMath[dist[temp_dist]] / counts[dist[temp_dist]]
            avgReading[dist[temp_dist]] = avgReading[dist[temp_dist]] / counts[dist[temp_dist]]
            avgWriting[dist[temp_dist]] = avgWriting[dist[temp_dist]] / counts[dist[temp_dist]]
            #print avgScores[temp_dist]
            #print temp_dist
            #print counts[dist[temp_dist]]
           # print i
            #print
        # Special case for the last distrcit
        elif i == len(dist)-1:
            #print avgScores[dist[i]]
            avgScores[dist[i]] = avgScores[dist[i]] / counts[dist[i]]
            avgMath[dist[temp_dist]] = avgMath[dist[temp_dist]] / counts[dist[temp_dist]]
            avgReading[dist[temp_dist]] = avgReading[dist[temp_dist]] / counts[dist[temp_dist]]
            avgWriting[dist[temp_dist]] = avgWriting[dist[temp_dist]] / counts[dist[temp_dist]]
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
    return avgScores, avgMath, avgReading, avgWriting, totTaken

# Print all the scores
def printScores(dbn, dist, borough, name, taken, read, math, write):
    print "NAME -- READING -- MATH -- WRITE"
    for x in range(len(dbn)):
        print name[x] + " -- " + read[x] + " -- " + math[x] + " -- " + write[x]

#  Print the scores by distrcit
def scoresByDist(scores, math, read, write, taken):
    for item in scores:
        print str(item) + " -------------- " + str(scores[item]) + " -------------- " + str(math[item]) + " -------------- " + str(read[item]) + " -------------- " + str(write[item]) + " -------------- " + str(taken[item])

# Combine the data-lists into a single dictionary
# Mapping preserved by index value between multiple lists is now maintained by a single key-- the distrcit.
def combineLists(scores, math, read, write, taken):
    combined_scores = {}
    for item in scores:
        combined_scores[item] = [scores[item], math[item], read[item], write[item], taken[item]]

    combined_sorted = collections.OrderedDict(sorted(combined_scores.items()))

    for elem in combined_sorted:
        print "| " + str(elem) + " | " + str(combined_sorted[elem][0]) + " | " + str(combined_sorted[elem][1]) + " | " + str(combined_sorted[elem][2]) + " | " + str(combined_sorted[elem][3]) + " | " + str(combined_sorted[elem][4]) + " |"

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
    tot_scores, math_scores, reading_scores, writing_scores, total_taken = calculateAverages(school_dbn, district_vals, boroughs, names, taken, read, math, write)
    combineLists(tot_scores, math_scores, reading_scores, writing_scores, total_taken)

    #printScores(school_dbn, district_vals, boroughs, names, taken, read, math, write)
