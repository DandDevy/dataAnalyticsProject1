#!/usr/bin/env python
# coding: utf-8

# In[72]:


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
    """
    This is a bar chart representing the workclass freqency per workclass per gender
    """
    print("\n\n --- task 1 ---\n\n\n")

    data = dataframeFromCSV.copy()[["workclass", "sex"]]
    data = data.dropna()

    data.sex = data["sex"].str.replace(" ", "")
    data.workclass = data["workclass"].str.replace(" ", "")
    data = data[data["workclass"] != "?"]
    data = data[data["sex"] != "?"]
#     print(data);
    #workclass_value_counts = data["workclass"].value_counts()
    
    df = data.groupby(["sex"])
#     print(df['workclass'].value_counts())
#     df['workclass'].value_counts().plot(kind='bar')
    
    data_male = data[data["sex"] != "Female"]
    data_female = data[data["sex"] != "Male"]
    print(data_male)
    print(data_female)
    data_wc = data["workclass"].unique().tolist()
    index = np.arange( len(data_wc))
    print(data_wc)
    print(data_male["workclass"].value_counts())
    
    fig, ax = plt.subplots()
    
    ax.bar(index, data_male["workclass"].value_counts(), 0.3,label=str(data_wc))
    ax.bar(index+0.3, data_female["workclass"].value_counts(), 0.3,label=str(data_wc))
    
    ax.set_xticklabels(data["workclass"].unique().tolist())
    ax.set_xticks(index + 0.3 / 2)
    ax.set_xticklabels(data["workclass"].unique().tolist(),rotation=90)
    ax.set_xlabel('workclass per gender')
    ax.set_ylabel('workclass frequency per workclass and gender')
    ax.set_title('workclass type frequency per gender')
    ax.legend(["male","female"])
#     plt.show()
    #workclass_value_counts.groupby(data["sex"])
#     df.plot(x ='sex', y=workclass_value_counts, kind = 'bar')

#     workclass_value_counts.plot(kind='bar');

#     plt.plot(workclass_value_counts)
    
#     data["sex"].value_counts().plot(kind='bar')
    # data["workclass"].value_counts().plot(kind="bar")
    # data.plot(x="workclass", y="sex",kind="bar")
    # print(data[[" workclass", "sex"]])

    
    #your implementation for task 1 goes here
   
    
task1()


# In[74]:


def task2():
    """
    This is a bar chart for the different frequencies of hours for each education
    """
    t2data = dataframeFromCSV.copy()[["hours-per-week","education", "sex"]]
    t2data = t2data.dropna()
    t2data.education = t2data.education.str.replace(" ", "")
    t2data.sex = t2data.sex.str.replace(" ", "")
#     print(t2data.education.unique())
#     print(t2data.sex.unique())
#     print(t2data["hours-per-week"].unique())
    t2data = t2data[t2data["sex"] != "Male"]
#     print(t2data["hours-per-week"].value_counts())
    t2edu_Masters = t2data[t2data["education"] == "Masters"]
#     print(len(t2edu_Masters["hours-per-week"].unique()))
    t2data_grped_edu = t2data.groupby(["education"])
#     print(t2data_grped_edu["hours-per-week"].unique())
#     print(t2data_grped_edu["hours-per-week"].unique().value_counts())
    fig, ax = plt.subplots()
    t2data["education"].value_counts().plot(kind='bar')
    ax.set_xlabel('education')
    ax.set_ylabel('frequency of different hours')
    ax.set_title('frequency of different hours for education')
    ax.legend(["education"])
#     print(t2data)
#     t2data2 = t2data.dropna()
#     print(t2data.head(32562))
#     print(t2data.columns)
#     print(t2data.head(3))
#     t2data3 = t2data.drop(0)
#     print(t2data3.head(3))
#     for i in range(len(t2data["hours-per-week"])):
#         value = t2data["education"][i]
#         if type(value) !=str:
#             t2data2 = t2data.drop(i)
# #             del t2data[i]
#     print(t2data2.head(32562))      
#     df = t2data2.groupby(["education","sex"])
 
# #     df.drop(32561)
#     print("df.head(32562):\n",df.head(32562))
#     plt.plot(t2data2["hours-per-week"],t2data2["sex"])
#     df.plot()
#     print(t2data)
    
    
task2()
"""
def task2():
    t2data = dataframeFromCSV.copy()[["hours-per-week","education", "sex"]]
    t2data = t2data.dropna()
    t2data.education = t2data.education.str.replace(" ", "")
    t2data.sex = t2data.sex.str.replace(" ", "")
    print(t2data.education.unique())
    print(t2data.sex.unique())
    print(t2data["hours-per-week"].unique())
    t2data = t2data[t2data["sex"] != "Male"]
#     print(t2data["hours-per-week"].value_counts())


#     t2data.plot(kind='scatter'x=)

    t2edu_Masters = t2data[t2data["education"] == "Masters"]
    print(len(t2edu_Masters["hours-per-week"].unique()))
    t2data_grped_edu = t2data.groupby(["education"])
    
    scatter_x = t2data_grped_edu.education.value_counts()
    scatter_y = t2data_grped_edu["hours-per-week"].value_counts()
    
    t2data_grped_edu.plot(kind='scatter', x=scatter_x, y=scatter_y)
    print(t2data_grped_edu["hours-per-week"].unique())
#     print(t2data_grped_edu["hours-per-week"].unique().count())
#     print(t2data_grped_edu["hours-per-week"].unique().count())
    
    t2data_grped_edu["hours-per-week"].value_counts().plot()
    t2data["education"].value_counts().plot(kind='bar')
#     print(t2data)
#     t2data2 = t2data.dropna()
#     print(t2data.head(32562))
#     print(t2data.columns)
#     print(t2data.head(3))
#     t2data3 = t2data.drop(0)
#     print(t2data3.head(3))
#     for i in range(len(t2data["hours-per-week"])):
#         value = t2data["education"][i]
#         if type(value) !=str:
#             t2data2 = t2data.drop(i)
# #             del t2data[i]
#     print(t2data2.head(32562))      
#     df = t2data2.groupby(["education","sex"])
 
# #     df.drop(32561)
#     print("df.head(32562):\n",df.head(32562))
#     plt.plot(t2data2["hours-per-week"],t2data2["sex"])
#     df.plot()
#     print(t2data)
    
    
task2()
"""


# In[75]:


def task3():
    """
    This is a bar chart representing the maximum entry of countries  
    """
    t3data = dataframeFromCSV.copy()
    t3data_withoutquestion_mark = t3data[t3data["native-country"] != " ?"]
    fig, ax = plt.subplots()
    t3data_withoutquestion_mark["native-country"].value_counts().plot(kind='bar')
    ax.set_xlabel('country')
    ax.set_ylabel('frequency')
    ax.set_title('frequency of country in data set and maximum entry of countries ')
    ax.legend(["country frequency"])
    
task3()


# In[76]:


def task4():
    """
    This is a bar chart representing the maximum entry of countries ignoring the maximum 
    """
    t4series = dataframeFromCSV.copy()["native-country"]
    t4series_without_nulls = t4series.dropna()
    t4data_withoutquestion_mark = t4series_without_nulls[t4series_without_nulls != " ?"]
    t4_countries_count = t4data_withoutquestion_mark.value_counts()
    fig, ax = plt.subplots()
    
    t4_countries_count_without_largest = t4_countries_count.drop(t4_countries_count.index[0])
    t4_countries_count_without_largest.plot(kind='bar')
    print(t4_countries_count_without_largest)
    ax.set_xlabel('country')
    ax.set_ylabel('frequency')
    ax.set_title('frequency of country in data set and maximum entry of countries outside top')
    ax.legend(["country frequency"])
#     t4data_country_counts = t4data
#     print(t4series)
task4()


# In[78]:


def task5():
    """
    This graph represents the line of the hours per week per age
    """
    t5df = dataframeFromCSV.copy()[["hours-per-week","age"]]
    t5df_no_null = t5df.dropna()
    t5df_no_null.education = t5df_no_null["age"][t5df_no_null["age"] != " ?"]
    t5df_no_null["hours-per-week"] = t5df_no_null["hours-per-week"][t5df_no_null["hours-per-week"] != " ?"]

    
    t5df_grp_by_hours = t5df_no_null.groupby(["hours-per-week"])
    print(t5df_grp_by_hours["age"].mean())
#     t5df_grp_by_hours["age"].mean().plot()
    
    t5df_grp_by_age = t5df_no_null.groupby(["age"])
    print(t5df_grp_by_age["hours-per-week"].mean())
#     t5df_grp_by_hours["hours-per-week"].value_counts()
#     print(t5df_grp_by_hours["hours-per-week"].value_counts())
    fig, ax = plt.subplots()
    
    t5df_grp_by_age["hours-per-week"].mean().plot()
    ax.set_xlabel('age')
    ax.set_ylabel('hours-per-week')
    ax.set_title('hours per week per age')
    ax.legend(["hours per week"])
#     t5df_grp_by_age_hours_mean = t5df_grp_by_age["hours-per-week"].mean()#.plot.scatter(x="x", y="y")
#     print(t5df_grp_by_age["hours-per-week"])
    
    
#     t5df_grp_by_hours.plot()
#     t5education_series = t5df_no_null["hours-per-week"].value_counts().plot(kind='bar')
#     t5df_grp_by_hours["education"].value_counts().plot(kind="scatter")
#     t5df_no_null.plot()
#     print(t5df_no_null)
task5()


# In[79]:


def task6():
    """
    This is a bar chart representing the outliers of education. Here we can see a difference between HS-grad compared to others and Bachelors,some college
    compared to others
    """
    t6df = dataframeFromCSV.copy()["education"]
    print(t6df)
    fig, ax = plt.subplots()
    t6df_value_counts = t6df.value_counts().plot(kind="bar")
    ax.set_xlabel('education')
    ax.set_ylabel('education frequency')
    ax.set_title('education frequency showing outliers')
    ax.legend(["education frequency"])
task6()


# In[80]:


def task12():
    """
    This is a bar chart representing the outliers of marital-status.
    """
    t12df = dataframeFromCSV.copy()["marital-status"]
    print(t12df.value_counts())
    fig, ax = plt.subplots()
    t12df.value_counts().plot(kind="bar")
    ax.set_xlabel('marital-status')
    ax.set_ylabel('marital-status frequency')
    ax.set_title('marital-status frequency showing outliers')
    ax.legend(["marital-status frequency"])
task12()


# In[84]:


def task8():
    t8df = dataframeFromCSV.copy()[["marital-status","education"]]
#     print(t8df)
    t8df_grped_by_mtl_status = t8df.groupby(["marital-status"])
    print(t8df_grped_by_mtl_status["education"].value_counts())
    t8df_grped_by_mtl_status["education"].value_counts().plot(kind='bar',figsize=(30,10),title="marital-status education frequency")
    t8df_grped_by_mtl_status["education"].value_counts()
    
    t8df_grped_by_edu_sum = t8df_grped_by_mtl_status["education"].value_counts()
    print(t8df_grped_by_edu_sum)
#     print(t8df_grped_by_edu["marital-status"].value_counts().plot(kind='bar', figsize=(30,10)))
    
task8()


# In[81]:


def task8improved():
    """
    Bar chart representing the education frequency per marital status
    """
    t8df = dataframeFromCSV.copy()[["marital-status","education"]]
    t8df = t8df.dropna()
    t8_educ = t8df["marital-status"].unique().tolist()
    print(t8_educ, len(t8_educ))
    index = np.arange( len(t8_educ))
    fig, ax = plt.subplots()
    ax.bar(index, t8df["marital-status"].value_counts(), 0.3,label=str(t8_educ))
    ax.set_xticklabels(t8_educ,rotation=90)
    ax.set_xticks(index)
    ax.set_xlabel('marital-status')
    ax.set_ylabel('education frequency')
    ax.set_title('marital-status education frequency')
    ax.legend(["marital-status frequency"])
    plt.show()
    
    
task8improved()


# In[10]:


def task7():
    """
    Income type per gender
    
    Income type frequency per gender bar chart. 
    I have primarily used
    https://stackoverflow.com/questions/53182452/python-create-bar-chart-comparing-2-sets-of-data 
    
    https://stackoverflow.com/questions/38294852/making-a-chart-bigger-in-size
    https://pythonprogramming.net/graph-visualization-python3-pandas-data-analysis/
    """
    t7df = dataframeFromCSV.copy()[["sex","Income"]]
    t7df=t7df.dropna()
    t7df.Income = t7df["Income"].str.replace(".", "")
    t7df.sex = t7df["sex"].str.replace(" ", "")
#     t7df.Income = t7df[t7df.Income == '<=50K.'] = '<=50K'
    print(t7df["sex"].unique())
    print(t7df["Income"].unique())
    t7_sex = t7df["Income"].unique()
    index = np.arange( len(t7_sex))
    t7_male = t7df[t7df["sex"] != "Female"]
    t7_female = t7df[t7df["sex"] != "Male"]
    fig, ax = plt.subplots()
    
    print(t7_male["Income"].value_counts().mean())
    print(t7_female["Income"].value_counts().mean())
    
    ax.bar(index, t7_male["Income"].value_counts(), 0.2,label=str(t7_sex))
    ax.bar(index+0.2, t7_female["Income"].value_counts(), 0.2,label=str(t7_sex))
    ax.set_xticklabels(t7df["Income"].unique().tolist())
    ax.set_xlabel('Income')
    ax.set_ylabel('frequency per gender')
    ax.set_title('Income type frequency per gender')
    ax.set_xticks(index + 0.2 / 2)
    ax.legend("MF")
    plt.show()
    
task7()


# In[11]:


def task9():
    """
    The frequency of occupation per marital-status and occupation
    """
    t9df = dataframeFromCSV.copy()[["marital-status","occupation"]]
    t9df = t9df.dropna()
    t9df["marital-status"] = t9df["marital-status"].str.replace(" ", "")
    t9df["occupation"] = t9df["occupation"].str.replace(" ", "")
    
    t9df = t9df[t9df["occupation"] != "?"]
    print(t9df["marital-status"].unique())
    print(t9df["occupation"].unique())
    
    print(t9df)
    t9ms = t9df["marital-status"].unique().tolist()
    index = np.arange(len(t9ms))
    t9o = t9df["occupation"].unique().tolist()
    index2 = np.arange(len(t9o))
    fig, ax = plt.subplots()
    t9_gp_by_ms=t9df.groupby(["marital-status"])
    print(t9_gp_by_ms["occupation"].value_counts())
#     ax.bar(index, t9_gp_by_ms["marital-status"].value_counts(), 0.35,label=t9ms)
#     ax.bar(index2, t9_gp_by_ms["occupation"].value_counts(), 0.35,label=t9o)
    ax.set_xticklabels(t9o,rotation=90)
    t9_gp_by_ms["occupation"].value_counts().plot(kind='bar',figsize=(30,15))
    ax.legend(["frequency of occupation"])
    ax.set_xlabel('occupation per marital-status')
    ax.set_ylabel('frequency of occupation')
    ax.set_title('frequency of occupation per marital-status')
#     t9_gp_by_ms["occupation"].value_counts().plot().bar(x=t9_gp_by_ms["occupation"].value_counts(),height=4)
    
task9()


# In[82]:


def task10():
    """
    bar chart of frequency of education per occupation
    """
    t10df = dataframeFromCSV.copy()[["education","occupation"]]
    t10df = t10df.dropna()
    t10df["occupation"] = t10df["occupation"].str.replace(" ", "")
    t10df["education"] = t10df["education"].str.replace(" ", "")
    t10df = t10df[t10df["occupation"] != '?']
    print(t10df["education"].unique())
    print(t10df["occupation"].unique())
    t10o = t10df["occupation"].unique()
    t7_Masters = t10df[t10df["education"]== "Masters"]
    t7_Bachelors = t10df[t10df["education"] == "Bachelors"]
    fig, ax = plt.subplots()
    index = np.arange(len(t10o))
    print(t7_Bachelors["occupation"].value_counts())
    width=np.arange(len(t10o))
    ax.bar(index, t7_Bachelors["occupation"].value_counts(), 0.1,label=str(t10o))
    ax.bar(index+0.1, t7_Masters["occupation"].value_counts(), 0.1,label=str(t10o))
    ax.set_xticklabels(t10df["occupation"].unique().tolist(),rotation=90)
    ax.set_xticks(index)
    ax.legend(["bachelors","masters"])
    ax.set_ylabel('frequency of education')
    ax.set_title('frequency of education per occupation')
    
task10()


# In[86]:


def task11():
    """
    bar chart representing the frequency of relationship for the private workclass
    """
    t11df = dataframeFromCSV.copy()[["relationship","workclass"]]
    t11df = t11df.dropna()
    t11df["relationship"] = t11df["relationship"].str.replace(" ", "")
    
    t11df["workclass"] = t11df["workclass"].str.replace(" ", "")
    t11df = t11df[t11df["workclass"] == 'Private']
    
    print(t11df["relationship"].unique())
    print(t11df["workclass"].unique())
    fig, ax = plt.subplots()
    t11df["relationship"].value_counts().plot(kind='bar')
    ax.legend(["relationship frequency"])
    ax.set_ylabel('frequency of relationship')
    ax.set_xlabel('relationship')
    ax.set_title('frequency of relationship for the private workclass')
    
    print(t11df)
task11()

