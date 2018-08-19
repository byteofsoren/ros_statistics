#!/usr/bin/env python
import os
import sys
import numpy as np
import pathlib
import scipy.stats


def get_data(argv):
    """Reads the logfile and search the file line by line. Then it checks if
    it got a match for the match variable. Then it convert that comes after
    in to a array and puts it in an numpy array and return it.

    :argv: a array of the given arguments
    :returns: returns a np.array

    """
    #path_to_logs = str(pathlib.Path.home()) + "/.ros/log/" + str(file_name)
    file_name = argv[1]
    match = argv[2]
    ret_array = list()
    if os.path.exists(file_name):
        fh = open(file_name)
        for line in fh:
            if str(match) in line:
                splitted = line.split(str(match))[1]
                row_arr = np.fromstring(splitted, sep=",")
                ret_array.append(row_arr)
    else:
        print("Incorrect filename")
    return np.array(ret_array)

def analyse(argv, array, confidence=0.95):
    """TODO: Analyse a np array for statistics

    :argv: array of given program arguments
    :array: np.array to analyze for data
    :returns: [Mean,low_c,hig_c] for each axis

    """
    if (len(argv) > 3) and (int(argv[3]) == 1):
        a = array.transpose()
    else:
        a = array
    ret_array = list()
    cols = a.shape[1]
    for c in range(cols):
        n = len(a[:,c])
        mean = np.mean(a[:,c])
        sem = scipy.stats.sem(a[:,c])
        conf = sem * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
        worst = max(a[:,c])
        best = min(a[:,c])
        ret_array.append([mean,mean-conf,mean+conf,n,confidence, best,worst])
    return ret_array

def show_data(array):
    """Show the data in an plessent way

    :array: an array containing analysed data
    :returns: None 

    """
    print("========================================")
    for row in array:
        print("Sample size: {}".format(row[3]))
        print("Mean: {m}\nConfidence interval {p}%:".format(m=row[0], p=row[4]*100))
        print("  {low} to {high}".format(low=row[1],high=row[2]))
        print("Best and worst case")
        print("  {best}, {worst}".format(best=row[5], worst=row[6]))
        print("\n========================================")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        data = get_data(sys.argv)
        analsed_data = analyse(sys.argv,data)
        show_data(analsed_data)
    else:
        print("ROS - log analyzer and statistic generator")
        print("stat.py [file] [keyword] [axis=0]")
        print("")
        print(":file:   \t is the log file you want to analyze")
        print(":keyword:\t is a key word you want to search for")
        print(":axis:   \t is in what 'direction' you want to analyse")
        print("  Default is 0 and generate statistic for columns\n   wile 1 is statistics of the current row")
        print("This will analyze the [file] for string containing:")
        print("keyword 13, 24, 42")
        print("Then reduce the information to:")
        print("13, 24, 42")
        print("After that dependent on what axis that was given it show the folowing:")
        print("Sample1. Sample size.")
        print("2. Mean,")
        print("3. Confidense intervall with 95%")
        print("4. Best and Worst case.")

