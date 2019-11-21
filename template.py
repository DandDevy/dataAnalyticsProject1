#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Secone assessment Programming for Data Analytic 
"""



# Please write your name and student ID:

# Daniel Ashcroft
# r00168428

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframeFromCSV = pd.read_csv("adult.csv")

dataframeFromCSV.columns = dataframeFromCSV.columns.str.replace(" ","")

WORK_PLACE_VALUE_TYPE = []



print("Daniel Ashcroft --- r00168428")
def task1():
    print("\n\n --- task 1 ---\n\n\n")

    data = dataframeFromCSV.copy()[["workclass", "sex"]]

    data.sex = data["sex"].str.replace(" ", "")
    data.workclass = data["workclass"].str.replace(" ", "")
    data = data[data["workclass"] != "?"]
    data = data[data["sex"] != "?"]
    print(data)
    df = pd.DataFrame({"hello":[1,5,1,2]})
    df.plot()
    # data["workclass"].value_counts().plot(kind="bar")
    # data.plot(x="workclass", y="sex",kind="bar")
    # print(data[[" workclass", "sex"]])

    # print(data["sex"])
    return True

    
    #your implementation for task 1 goes here
   
    
task1()
#comment for task1: 
    
def task2():
    return True
    
    #your implementation for task 2 goes here
   
    
    
#comment for task2: 
    
def task3():
    return True
    
    #your implementation for task 3 goes here
   
    
    
#comment for task3: 
    
def task4():
    return True
    
    #your implementation for task 4 goes here
   
    
    
#comment for task4: 
    
def task5():
    return True
    
    #your implementation for task 5 goes here
   
    
    
#comment for task5: 
    
def task6():
    return True
    
    #your implementation for task 6 goes here
   
    
    
#comment for task6: 
    
def task7():
    return True
    
    #your implementation for task 7 goes here
   
    
    
#comment for task7: 
    
def task8():
    return True
    
    #your implementation for task 8 goes here
   
    
    
#comment for task8: 
    
def task9():
    return True
    
    #your implementation for task 9 goes here
   
    
    
#comment for task9: 
    
def task10():
    return True
    
    #your implementation for task 10 goes here
   
    
    
#comment for task10: 
    
    
def task11():
    return True
    
    #your implementation for task 11 goes here
   
    
    
#comment for task11: 
    
def task12():
    return True
    
    #your implementation for task 12 goes here
   
    
    
#comment for task12: 