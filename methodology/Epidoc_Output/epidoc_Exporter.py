## James M. Tucker, PhD (cand.)
## University of Toronto

import os, sys, re
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json


def check_line(l, accrue):
    '''
    This function accumulates the line_ID of the DataFrame so that a newline can be added
    when the line increments by one.
    '''
    
    #check current line_ID against the previous
    if l == a
        #If the line nums are the same send back false
        r = 0
    elif l != accrue[-1]:
        #if the line numbers differ send back true
        r = 1

    #append the current line to the array to check for the next
    accrue.append(l)
    
    last_seen = accrue[-1]
    return(r)

def process_CSV(csv_file, out_file, opt):
    tei = [] #this generates a list of attributes from attr_0

    #create a Pandas Dataframe
    df = pd.read_csv(csv_file)

    #order dataframe on the reading order for SQL database input
    df.set_index('reading_Order', inplace=True)
    
    #create BKP file and order on the reading order
    df.to_csv(out_file)

    #create an accrue array to find line breaks on fragment
    accrue = [1]

    for index, row in df.iterrows():
        #pass the line num through the validator
        line_Num = check_line(row['line_ID'], accrue)

        if line_Num == 0:
            #todo build line
            if str(row['uni_He_0']) == ' ':
                pass
                #todo on character
            else:
                pass
        elif line_Num == 1:
            print("\t</li>")
            print("\t<li id=\"" + str(row['line_ID']) + "\">")