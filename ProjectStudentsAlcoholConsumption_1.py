#!/usr/bin/env python
# coding: utf-8

#st.subheader("Student Alcohol Consumption")

#st.subheader("Introduction")
#st.write("In this project, I want to consider the impact of various factors on alcohol consumption by students, as well as the impact of alcohol consumption on student academic performance.")
# Here is a transcript of each of the values:
# ###
# 1. school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
# 2. sex - student's sex (binary: 'F' - female or 'M' - male)
# 3. age - student's age (numeric: from 15 to 22)
# 4. address - student's home address type (binary: 'U' - urban or 'R' - rural)
# 5. famsize - size of the family (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
# 6. Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
# 7. Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
# 8. Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
# 9. Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
# 10. Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
# 11. reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
# 12. guardian - student's guardian (nominal: 'mother', 'father' or 'other')
# 13. traveltime - commute to school time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
# 14. studytime - number of teaching hours (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
# 15. failures - number of class failures in the past (numeric: n if 1<=n<3, else 4)
# 16. schoolsup - if student have a scholarship (binary: yes or no)
# 17. famsup - family educational support (binary: yes or no)
# 18. paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
# 19. activities - extracurricular activities (binary: yes or no)
# 20. nursery - if student attended nursery school (binary: yes or no)
# 21. higher - wants to take higher education (binary: yes or no)
# 22. internet - Internet access at home (binary: yes or no)
# 23. romantic - with a romantic relationship (binary: yes or no)
# 24. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
# 25. freetime - free time after school (numeric: from 1 - very low to 5 - very high)
# 26. goout - going out with friends (numeric: from 1 - very low to 5 - very high)
# 27. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 28. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 29. health - current health status (numeric: from 1 - very bad to 5 - very good)
# 30. absences - number of school absences (numeric: from 0 to 93)
# 31. G1 - first semester grade (numeric: from 0 to 20)
# 32. G2 - second semester grade (numeric: from 0 to 20)
# 33. G3 - final grade (numeric: from 0 to 20, output target)

# In[82]:


# !pip install pandas
# !pip install numpy
# !pip install plotly
# !pip install scipy
# !pip install pytelegrambotapi
# !pip install python-telegram-bot
# get_ipython().system('pip install streamlit')

import pandas as pd
import numpy as np
import streamlit as st
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
# import scipy.stats
# import matplotlib.plotly_chart as plt
from collections import Counter
import itertools
# import telebot
# from telebot import types
import logging
import streamlit as st

# from telegram.ext import (CommandHandler, ConversationHandler, Filters,
#                          MessageHandler, Updater)
# from telegram import ReplyKeyboardMarkup
st.title("Student Alcohol Consumption")

st.subheader("Introduction")
st.write("In this project, I want to consider the impact of various factors on alcohol consumption by students, as well as the impact of alcohol consumption on student academic performance.")

st.subheader("Let's see what data we will work with.")

st.write(" 1. school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)")
st.write(" 2. sex - student's sex (binary: 'F' - female or 'M' - male)")
st.write(" 3. age - student's age (numeric: from 15 to 22)")
st.write(" 4. address - student's home address type (binary: 'U' - urban or 'R' - rural)")
st.write(" 5. famsize - size of the family (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)")
st.write(" 6. Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)")
st.write(" 7. Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)")
st.write(" 8. Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)")
st.write(" 9. Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
st.write(" 10. Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
st.write(" 11. reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')")
st.write(" 12. guardian - student's guardian (nominal: 'mother', 'father' or 'other')")
st.write(" 13. traveltime - commute to school time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)")
st.write(" 14. studytime - number of teaching hours (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)")
st.write(" 15. failures - number of class failures in the past (numeric: n if 1<=n<3, else 4)")
st.write(" 16. schoolsup - if student have a scholarship (binary: yes or no)")
st.write(" 17. famsup - family educational support (binary: yes or no)")
st.write(" 18. paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
st.write(" 19. activities - extracurricular activities (binary: yes or no)")
st.write(" 20. nursery - if student attended nursery school (binary: yes or no)")
st.write(" 21. higher - wants to take higher education (binary: yes or no)")
st.write(" 22. internet - Internet access at home (binary: yes or no)")
st.write(" 23. romantic - with a romantic relationship (binary: yes or no)")
st.write(" 24. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)")
st.write(" 25. freetime - free time after school (numeric: from 1 - very low to 5 - very high)")
st.write(" 26. goout - going out with friends (numeric: from 1 - very low to 5 - very high)")
st.write(" 27. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
st.write(" 28. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
st.write(" 29. health - current health status (numeric: from 1 - very bad to 5 - very good)")
st.write(" 30. absences - number of school absences (numeric: from 0 to 93)")
st.write(" 31. G1 - first semester grade (numeric: from 0 to 20)")
st.write(" 32. G2 - second semester grade (numeric: from 0 to 20)")
st.write(" 33. G3 - final grade (numeric: from 0 to 20, output target)")
# In[83]:


alcohol = pd.DataFrame(
    pd.read_csv('student_mat.csv', sep=','))
st.write(alcohol)

#st.title("Contest from streamlit")
#st.header("")
#st.markdown("")
#st.subheader("")
#st.code("")
#st.header("ProjectStudentsAlcoholConsumption_1")
#st.markdown("Finaly")
st.subheader("Data cleanup")

st.write("As we can see, the information presented in the table is complete and does not require cleaning")

# In[84]:

#alcohol.info()
st.write("Output of the number of null")
st.write(alcohol.isnull().sum())
#st.write(alcohol.dtypes.count())
st.write(alcohol.shape)
#st.write(alcohol.info)

st.subheader("Data transformation")

st.write("Here I am adding 3 columns, with each  I will work with in the futher.")
st.write("1. I normalized the average alcohol consumption of a person for a week (the original dataset contains 2 columns Walk and Walk), that is, alcohol consumption on weekends and working days. I combined them into one Alc column by adding and dividing by 2 (this will give us the average value).")
st.write("2. I normalized the average amount of time spent studying, that is, I added the studytime parameter with a weight of 1 and the traveltime parameter with a weight of 0.1, since in the original dataset, the time spent on studying is considered 10 times more than the time spent on a trip to an educational institution. For example, to get 5 points for studies, a person must study 10 or more hours a week, and to get 5 points for the traveltime parameter, a person must spend 1 hour or more per week on a trip to an educational institution.")
st.write("3. Finally, I changed the binary F and M in the sex column to 1 and 0.")

# In[85]:


alcohol = alcohol.assign(Alc=(alcohol.Dalc + alcohol.Walc) / 2)
alcohol = alcohol.assign(AllStudytime=(alcohol.studytime + alcohol.traveltime * 0.1))
alcohol.sex = alcohol.sex.apply([lambda x: 0 if x == 'F' else 1])
pd.set_option('display.max_columns', None)
alc1 = alcohol[['sex','Alc','AllStudytime']]
st.write(alc1)

st.subheader("Descriptive statistics")

# In[86]:


#print(f'Shape of the dataset: {alcohol.shape[0]} rows by {alcohol.shape[1]} columns')
st.write(f'Shape of the dataset: {alcohol.shape[0]} rows by {alcohol.shape[1]} columns')
# In[87]:


st.write('Number of girls:', alcohol[alcohol['sex'] == 0].shape[0])
st.write('Number of boys:', alcohol[alcohol['sex'] == 1].shape[0])

# In[88]:


st.write('Number of people with internet at home:', alcohol[alcohol['internet'] == 'yes'].shape[0])
st.write('Number of people without internet at home:', alcohol[alcohol['internet'] == 'no'].shape[0])

# In[89]:


st.write('Number of people of age 15:', alcohol[alcohol['age'] == 15].shape[0])
st.write('Number of people of age 16:', alcohol[alcohol['age'] == 16].shape[0])
st.write('Number of people of age 17:', alcohol[alcohol['age'] == 17].shape[0])
st.write('Number of people of age 18:', alcohol[alcohol['age'] == 18].shape[0])
st.write('Number of people of age 19:', alcohol[alcohol['age'] == 19].shape[0])
st.write('Number of people of age 20:', alcohol[alcohol['age'] == 20].shape[0])
st.write('Number of people of age 21:', alcohol[alcohol['age'] == 21].shape[0])
st.write('Number of people of age 22:', alcohol[alcohol['age'] == 22].shape[0])

# In[90]:


alcohol_anal = alcohol[['age', 'Alc', 'G3', 'famrel', 'freetime']].describe().drop(['25%', '50%', '75%'])
st.write(alcohol_anal)

# In[91]:


alcohol_med = [
    ['median', alcohol['age'].median(), alcohol['Alc'].median(), alcohol['G3'].median(), alcohol['famrel'].median(),
     alcohol['freetime'].median()]]
alcohol_mediana = pd.DataFrame(alcohol_med, columns=['value', 'age', 'Alc', 'G3', 'famrel', 'freetime'])
alcohol_mediana

st.subheader("Let's look at some average values from the dataset.")
st.write("1. We can see that the average age of respondents is 17 years old. There is also a significant deviation of 1.28 points, which means that we also have a lot of 16 and 18-year-old students (we will check this later).")
st.write("2. It may seem strange but alcohol consumption is relatively small, only 1.88 points out of 5, which means that most students consume little alcohol but again we see a large variance that reached 1.29 points.")
st.write("3. At the same time, we can see that most of the people who passed the survey, studied well, anyway, the spread of the value is very big (4.58 points).")
st.write("4. We can also see that most students have good family relations (3.94 points out of 5), but again we see a large variance of 0.9 points).")
st.write("5. We can also see that the majority of respondents have a lot of free time, since the average value is 4 (out of 5) and the deviation relatively small, only 1 point. In the future, it is worth checking the correlation of free time and alcohol consumption.")

st.subheader("Overview")

st.write("Let's look at the simple pie chart 'Internet conection of the respondents', the bar chart 'Number of people of each age' and the more complex bar chart 'Exam grades' with a trend line and also the line chart 'Alcohol consumption'")

# In[92]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(x=alcohol['Alc'].value_counts().sort_index().index, y=alcohol['Alc'].value_counts().sort_index()))
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="Alcohol consumption",
    title_x=0.5,
    xaxis_title="Frequency of alcohol consumption by respondents",
    yaxis_title="Number of the respondents",
    legend=dict(x=.5, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=30, b=0),
    bargap=0.2)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")

# In[93]:


df = alcohol.sex
number_of_people_with_and_without_internet = [alcohol[alcohol['internet'] == 'yes'].shape[0],
                                              alcohol[alcohol['internet'] == 'no'].shape[0]]
names_of_the_values = ['Number of people with internet at home', 'Number of people without internet at home']
fig = px.pie(df, values=number_of_people_with_and_without_internet, names=names_of_the_values)
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="Distribution of people by internet connection",
    title_x=0.5,
    legend=dict(x=.5, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=30, b=0))
# fig.show()
st.plotly_chart(fig)

# In[94]:


data = alcohol.age
number_of_people_of_age = [alcohol[alcohol['age'] == 15].shape[0], alcohol[alcohol['age'] == 16].shape[0],
                           alcohol[alcohol['age'] == 17].shape[0], alcohol[alcohol['age'] == 18].shape[0],
                           alcohol[alcohol['age'] == 19].shape[0], alcohol[alcohol['age'] == 20].shape[0],
                           alcohol[alcohol['age'] == 21].shape[0], alcohol[alcohol['age'] == 22].shape[0]]
names_of_the_values = ['Number of people of age 15', 'Number of people of age 16', 'Number of people of age 17', 'Number of people of age 18', 'Number of people of age 19', 'Number of people of age 20','Number of people of age 21', 'Number of people of age 22']
fig = px.bar(data, y=number_of_people_of_age, x=names_of_the_values, color=names_of_the_values)
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="Distribution of people by age",
    title_x=0.5,
    # xaxis.set_visible(False),
    xaxis_title="Age of the respondents",
    yaxis_title="Number of the respondents",
    legend=dict(x=.5, xanchor="center", orientation="h", bgcolor='black'),
    margin=dict(l=0, r=0, t=30, b=0),
    bargap=0.1
)
fig.update_xaxes(visible=False)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")

# In[95]:


fig = go.Figure(data=[
    go.Histogram(x=alcohol['G3'], name='number of people who recieved each grade', marker=dict(color="LightSeaGreen"))])

smoothTrace = {
    'type': 'scatter',
    'mode': 'lines',
    'x': alcohol['G3'].value_counts().sort_index().index,
    'y': alcohol['G3'].value_counts().sort_index(),
    'line': {'shape': 'spline', 'smoothing': 1.3}

}

fig.add_trace(go.Scatter(smoothTrace, name='trade line'))
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="The number of people who received each grade",
    title_x=0.5,
    xaxis_title="English exam grade of the respondents",
    yaxis_title="Number of the respondents",
    legend=dict(x=.5, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=30, b=0),
    bargap=0.1,width=600, height=600)
# fig.update_traces(line_color='#0000ff', line_width=5)
# fig.update_traces(marker_line_color='green', selector=dict(type='histogram'))
# plt.fig(color='green')
# fig.show()
fig.update_xaxes(visible=True)
st.plotly_chart(fig, use_container_width=True,theme="streamlit")

st.subheader("More detailed overview")

st.write("In this part I will look at correlations and build complex graphs. However, I will build complex graphs only for those quantities for which there is a significant correlation.")
st.write("You should familiarize yourself with the correlation values:")
st.write("Correlation                   Connection")
st.write("0.00 - 0.24                     very weak connection")
st.write("0.24 - 0.49                     average connection")
st.write("0.49 - 0.75                     strong connection")
st.write("0.75 - 1.00                     very strong connection")

st.write("I decided to divide the correlation coefficients into two subtypes: positive and negative. And also distribute them in descending order.")

# ### Positive correlations

# Let's look at the correlation of free time and alcohol consumption.
# My guess is that the more you go out with friends, the more you drink.

# In[96]:


#print(np.corrcoef(alcohol['Alc'], alcohol['goout'])[0, 1])
st.subheader("Positive correlations")
data_corr = pd.DataFrame(data=alcohol, columns=['Alc', 'failures', 'absences', 'age', 'health', 'sex', 'goout', 'freetime'])
#display(data_corr.corr())
st.write(data_corr.corr())
fig_corr1 = px.scatter_matrix(data_corr)
fig_corr1.update_layout(width=600, height=600)
st.plotly_chart(fig_corr1,use_container_width=True,theme="streamlit")

st.write("Let's look at the correlation of free time and alcohol consumption. My guess is that the more you go out with friends, the more you drink.")



a1 = np.corrcoef(alcohol['Alc'], alcohol['goout'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['goout'])[0, 1]")
st.write(a1)

# In[97]:



#fig1 = pd.plotting.scatter_matrix(data_corr, figsize=(20, 10))
#plt.show()
#st.vega_lite_chart(fig1)

st.write("Hooray! There is a correlation and it is quite strong, let's visualize it!")

# In[98]:


small_free_time1 = alcohol['freetime'] < 3
much_free_time1 = alcohol['freetime'] >= 3
small_free_time = alcohol[small_free_time1]
much_free_time = alcohol[much_free_time1]
fig = go.Figure()
fig.add_trace(go.Bar(x=small_free_time['Alc'].value_counts().sort_index().index,
                     y=small_free_time['Alc'].value_counts().sort_index(), name='people with less free time'))
fig.add_trace(go.Bar(x=much_free_time['Alc'].value_counts().sort_index().index,
                     y=much_free_time['Alc'].value_counts().sort_index(), name='people with much free time'))
fig.update_layout(barmode='stack',title=dict(xanchor= 'center'),
                  title_text="The consumption of the alcohol for people with much and less free time",
                  title_x=0.5,
                  xaxis_title="Frequency of alcohol consumption by the respondents",
                  yaxis_title="Number of the respondents",
                  legend=dict(x=.5, xanchor="center", orientation="h"),
                  margin=dict(l=0, r=0, t=30, b=0),width=1000, height=600)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")


st.write("The resulting graph shows that alcohol consumption increases with the increase in the number of parties with friends. This may be due to the fact that students like to drink in the company, and accordingly fall into the drinking company, with which they often go to bars and clubs.")

st.write("Let's look at the correlation between sex and the degree of alcohol consumed.")

# In[99]:


#print(np.corrcoef(alcohol['Alc'], alcohol['sex'])[0, 1])
a2 = np.corrcoef(alcohol['Alc'], alcohol['sex'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['sex'])[0, 1]")
st.write(a2)
# In[99]:


st.write("Let's look at alcohol consumption among men and women separately. I will assume that men drink alcohol more than women.")

# In[100]:


female1 = alcohol['sex'] == 0
male1 = alcohol['sex'] > 0
female = alcohol[female1]
male = alcohol[male1]

fig = go.Figure()
fig.add_trace(go.Histogram(x=male['Alc'], name='men', marker=dict(color="#082567")))
fig.add_trace(go.Histogram(x=female['Alc'], name='women', marker=dict(color="#ffd800")))
fig.update_layout(title=dict(xanchor= 'center'),
                  title_text="The consumption of the alcohol of men and women",
                  title_x=0.5,
                  xaxis_title="Frequency of alcohol consumption by the respondents",
                  yaxis_title="Number of the respondents",
                  legend=dict(x=.5, xanchor="center", orientation="h"),
                  margin=dict(l=0, r=0, t=30, b=0),width=1000, height=600)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")

st.write("The resulting graph confirms my assumption. This may be related to the biological and psychological characteristics of people of different sexes.")

st.write("Let's look at the correlation between alcohol and the amount of free time. My guess is that the more free time you have, the more you drink.")

# In[101]:


a3 = np.corrcoef(alcohol['Alc'], alcohol['freetime'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['freetime'])[0, 1]")
st.write(a3)

st.write("And indeed, there is a fairly strong correlation.  This may be due to the fact that people simply have nothing to occupy themselves with, and taking alcohol becomes their main entertainment.")

st.write("Other correlations are too insignificant (they are given below), so it makes no sense to consider them further in the project.")

# In[102]:

st.write("correlation of the amount of alcohol consumed and failures")
a4 = np.corrcoef(alcohol['Alc'], alcohol['failures'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['failures'])[0, 1]")
st.write(a4)
# In[103]:

st.write("correlation of the amount of alcohol consumed and abscences")
a5 = np.corrcoef(alcohol['Alc'], alcohol['absences'])[0, 1]  # correlation of the amount of alcohol consumed and abscences
st.code("np.corrcoef(alcohol['Alc'], alcohol['absences'])[0, 1]")
st.write(a5)
# In[104]:

st.write("correlation of the amount of alcohol consumed and age")
a6 = np.corrcoef(alcohol['Alc'], alcohol['age'])[0, 1]  # correlation of the amount of alcohol consumed and age
st.code("np.corrcoef(alcohol['Alc'], alcohol['age'])[0, 1]")
st.write(a6)
# In[105]:

st.write("correlation of the amount of alcohol consumed and health")
a7 = np.corrcoef(alcohol['Alc'], alcohol['health'])[0, 1]  # correlation of the amount of alcohol consumed and health
st.code("np.corrcoef(alcohol['Alc'], alcohol['health'])[0, 1]")
st.write(a7)

st.subheader("Trivial, but interesting things in visualization")

st.write("Everyone thinks that girls study better than boys, let's check it out!")

# In[106]:


female1 = alcohol['sex'] == 0
male1 = alcohol['sex'] > 0
female = alcohol[female1]
male = alcohol[male1]
fig = go.Figure()
fig.add_trace(go.Scatter(x=male['AllStudytime'].value_counts().sort_index().index,
                         y=male['AllStudytime'].value_counts().sort_index(), name='men', mode='lines+markers',
                         line=dict(color="#082567")))
fig.add_trace(go.Scatter(x=female['AllStudytime'].value_counts().sort_index().index,
                         y=female['AllStudytime'].value_counts().sort_index(), name='women', mode='lines+markers',
                         line=dict(color="#ffff00")))
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="Study time of men and women",
    title_x=0.5,
    xaxis_title="Frequency of alcohol consumption by the respondents",
    yaxis_title="Number of the respondents",
    legend=dict(x=.5, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=30, b=0),
    bargap=0.2,width=1000, height=600)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")

st.write("Indeed, girls study more than boys (this can be seen by the fact that the red line is almost always higher than the blue one, which means that on average the amount of time spent studying is more). This can again be explained by the biological and physiological differences of both sexes.")

st.subheader("Negative correlations")
data_corr1 = pd.DataFrame(data=alcohol, columns=['Alc', 'famrel', 'Medu', 'Fedu', 'AllStudytime'])
#display(data_corr.corr())
st.write(data_corr1.corr())
fig_corr2 = px.scatter_matrix(data_corr1)
fig_corr2.update_layout(width=600, height=600)
st.plotly_chart(fig_corr2,use_container_width=True,theme="streamlit")

st.write("Let's look at the correlation between the amount of alcohol consumed and the time spent studying. I think the more you study, the less alcohol you consume.")


# In[107]:

n1 = np.corrcoef(alcohol['Alc'], alcohol['AllStudytime'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['AllStudytime'])[0, 1]")
st.write(n1)

# In[108]:


#data_corr = pd.DataFrame(data=alcohol, columns=['Alc', 'failures', 'absences', 'age', 'health', 'sex', 'AllStudytime'])
#write(data_corr.corr())

#pd.plotting.scatter_matrix(data_corr, figsize=(20, 10))
#plt.show()

st.write("Indeed, there is a rather strong negative correlation. Let's look at the visualization.")

# In[109]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(x=alcohol['Alc'].value_counts().sort_index().index, y=alcohol['Alc'].value_counts().sort_index(),
               name='alcohol'))
fig.add_trace(go.Scatter(x=alcohol['AllStudytime'].value_counts().sort_index().index,
                         y=alcohol['AllStudytime'].value_counts().sort_index(), name='study'))
fig.update_layout(title=dict(xanchor= 'center'),
    title_text="Alcohol consumption",
    title_x=0.5,
    xaxis_title="Frequency of alcohol consumption and time spent studying by respondents",
    yaxis_title="Number of the respondents",
    legend=dict(x=.5, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=30, b=0),
    bargap=0.2,width=1000, height=600)
# fig.show()
st.plotly_chart(fig,use_container_width=True,theme="streamlit")

st.write("This correlation quite logical, the more you study => the less free time => the less time for partying with friends. All other correlations are insignificant.")

st.write("The remaining correlations are insignificant, their coefficient is much lower than 0.24.")

# In[110]:

st.write("correlation between alcohol and family relationships")
n2 = np.corrcoef(alcohol['Alc'], alcohol['famrel'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['famrel'])[0, 1]")  # correlation between alcohol and family relationships
st.write(n2)
# In[111]:

st.write("correlation between alcohol and mother's education")
n3 = np.corrcoef(alcohol['Alc'], alcohol['Medu'])[0, 1]  # correlation between alcohol and mother's education
st.code("np.corrcoef(alcohol['Alc'], alcohol['Medu'])[0, 1]")
st.write(n3)
# In[112]:

st.write("correlation between alcohol and father's education")
n4 = np.corrcoef(alcohol['Alc'], alcohol['Fedu'])[0, 1]
st.code("np.corrcoef(alcohol['Alc'], alcohol['Fedu'])[0, 1]")  # correlation between alcohol and father's education
st.write(n4)

st.subheader("A main hypothesis check")

st.write("My hypothesis is that I believe that a lot of free time for girls and a lot of partying with friends lead to increase in alcohol consumption. I chose these values because they are the ones that are most positively correlated with alcohol: sex, amount of free time and hanging out with friends.")

# In[113]:


female1 = alcohol['sex'] == 0
male1 = alcohol['sex'] > 0
female = alcohol[female1]
male = alcohol[male1]

fig = go.Figure(data=[go.Mesh3d(x=female['goout'],
                                y=female['freetime'],
                                z=female['Alc'],
                                opacity=0.5,
                                color='deeppink')])

fig.update_layout(
    scene=dict(xaxis_title='goouts',yaxis_title='freetime',zaxis_title='alcohol consumption',
        xaxis=dict(nticks=4, range=[0, 5], ),
        yaxis=dict(nticks=4, range=[0, 5], ),
        zaxis=dict(nticks=4, range=[0, 5], ), ),
    width=1000,
    margin=dict(r=20, l=10, b=10, t=10),
    #title="Correlation between free time, goouts and frequency of alcohol consumption",
    title_x=0.5,
    xaxis_title="goouts",
    yaxis_title="freetime")
    #legend=dict(x=.5, xanchor="center", orientation="h"), height=600)
# fig.show()
st.plotly_chart(fig,use_container_width=True)#,theme="streamlit")

st.write("We can see that the graph has the shape of a mountain with a peak at point (5,5,5) (almost perfect correlation), which confirms our hypothesis: alcohol consumption is maximal at the point where other parameters are maximal. The irregularities of this mountain can be explained by insufficient sampling, if it were larger, the graph would have the shape of a triangle with a vertex at the same point.")

st.subheader("Web interface")

st.subheader("Telegram bot")

st.write("You can find bot by this link t.me/Alcash1bot")

# In[ ]:


st.code("logging.basicConfig(filename='bot.log', level=logging.INFO)")


code = '''def dialog_sex(update, context):
    reply_keyboard = [['Мужской'], ['Женский']]
    update.message.reply_text(
        'Пожалуйста, выберите ваш пол:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'time'")


def dialog_time(update, context):
    sex = update.message.text
    if sex == 'Мужской':
        context.user_data['dialog'] = {'sex': 1}
    elif sex == 'Женский':
        context.user_data['dialog'] = {'sex': 0}
    update.message.reply_text(
        'Сколько у вас свободного времени по шкале от 1 до 5?',
        reply_markup=digits_keyboard()
    )

    return "friends"


def dialog_friends(update, context):
    context.user_data['dialog']['time'] = int(update.message.text)
    update.message.reply_text(
        'По шкале от 1 до 5 – как часто вы встречаетесь с друзьями?',
        reply_markup=digits_keyboard()
    )

    return 'ending'

def dialog_ending(update, context):
    context.user_data['dialog']['friends'] = int(update.message.text)
    sex = context.user_data['dialog']['sex']
    free_time = context.user_data['dialog']['time']
    times_with_friends = context.user_data['dialog']['friends']

    result = (times_with_friends * 9) + (free_time * 9) + 10 * sex

    update.message.reply_text(
        f'Риск подверженности алкоголизму {result}%!',
        reply_markup=main_keyboard()
    )

    return ConversationHandler.END


def dialog_dontknow(update, context):
    update.message.reply_text(
        'Кажется, вы прислали мне что-то не то!'
    )


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Посчитать степень алкоголизма']]
    )


def digits_keyboard():
    return ReplyKeyboardMarkup(
        [['1', '2', '3', '4', '5']]
    )


def greet_user(update, context):
    user = update.effective_user
    update.message.reply_text(
        f'Привет, {user.first_name}! Если хочешь узнать степень своего алкоголизма, просто напиши мне «Посчитать степень алкоголизма»',
        reply_markup=main_keyboard()
    )


def main():
    mybot = Updater('5807673465:AAHGUxfVfoH7SyrBkablRY8nmYhEhbnMB8w')
    dp = mybot.dispatcher

    dialog = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Посчитать степень алкоголизма|посчитать степень алкоголизма)$'),
            dialog_sex)],
        states={'time': [MessageHandler(Filters.regex(
            '^(Мужской|Женский)$'), dialog_time)],
            'friends': [MessageHandler(Filters.regex(
                '^(1|2|3|4|5)$'), dialog_friends)],
            'ending': [MessageHandler(Filters.regex(
                '^(1|2|3|4|5)$'), dialog_ending)]},
        fallbacks=[MessageHandler(Filters.text | Filters.video |
                                  Filters.photo | Filters.document |
                                  Filters.location | Filters.attachment, dialog_dontknow)])

    dp.add_handler(dialog)
    dp.add_handler(CommandHandler("start", greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


#if __name__ == "__main__":'''
#    main()
st.code(code,language='python')
# In[ ]:


# In[ ]:


# In[ ]:

