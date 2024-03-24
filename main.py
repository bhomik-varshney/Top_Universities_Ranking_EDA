import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('./university.csv')
data1 = np.array(data)
print(data.columns)
print(data1[0:5])
data.rename(columns ={'ranking-institution-title':'Name'}, inplace =True)
print(data.columns)
print(data.isnull().sum()) #12 null values for location.
data.fillna('No',inplace=True)
print(data.isnull().sum())


x = data.groupby(['rank','Name'])['rank'].min().head(10)
print(x)
# 1     Massachusetts Institute of Technology
# 2     Stanford University
# 3     Harvard University
# 4     University of California, Berkeley
# 5     University of Cambridge
# 6     University of Oxford
# 7     The University of Chicago
# 8     Tsinghua University
# 9     Yale University
# 10    Peking University

# plt4 = px.histogram(data,x='location', marginal='box',color_discrete_sequence=['red'])
# plt4.show()

x1 = data.groupby(['rank','Name','location'])['rank'].min().head(10)
print(x1)
#top 4 universitites are of United States.

x2 = data[data['location']=='India'].groupby(['rank','Name'])['rank'].min()
print(x2)
#rank   Name     (India's top universities)
# 440   Jamia Millia Islamia
# 505   Aligarh Muslim University
# 506   Amity University
# 510   Banaras Hindu University
# 522   University of Delhi

x3 = data.groupby(['Name','Research Quality Score'],as_index=False)['Research Quality Score'].max().sort_values(by ='Research Quality Score',ascending =False).head(10)
print(x3)
# Worcester Polytechnic Institute                    98.6    (top research universities)
# Lappeenranta-Lahti University of Technology LUT                    97.9
# Beijing Institute of Technology                    97.8
# University of Sharjah                    97.5
# Free University of Bozen-Bolzano                    97.5
# Swansea University                    97.1
# The University of Chicago                    95.8
# University of Surrey                    95.4
# Harvard University                    95.2
# University of Plymouth                95.2
x4 = data[data['location']=='India'].groupby(['Name','Research Quality Score'],as_index=False)['Research Quality Score'].max().sort_values(by ='Research Quality Score',ascending =False).head(10)
print(x4)
#               Amity University                    79.2 (top research university of india)
#       Lovely Professional University                    76.4
#                 Jamia Millia Islamia                    73.8
#         Aligarh Muslim University                    62.7
#          Banaras Hindu University                    61.3
#   Symbiosis International University                    60.4
#       Delhi Technological University                    57.2
#                   Panjab University                    52.4
#                                UPES                    47.3
#               University of Delhi                      42.8

data['Research Quality Score range']=  pd.qcut(data['Research Quality Score'],5)

# x5 = data.groupby(['location','Research Quality Score range'],as_index=False)['location'].count().sort_values(by='location',ascending = False).head(7)
# sns.countplot(x= 'location', data = x5)
# plt.show()
# print(x5)

print(data['Research Quality Score range'].describe())
x6 = data.groupby(['Research Quality Score range'])['Research Quality Score range'].count()
print(x6)
data['Research Quality Score category'] = 0
y1 = data.loc[(data['Research Quality Score']<=43.4),'Research Quality Score']= 1
y2 = data.loc[(data['Research Quality Score']>43.4)& (data['Research Quality Score']<=58.06),'Research Quality Score category']= 2
y3 = data.loc[(data['Research Quality Score']>58.06)& (data['Research Quality Score']<=69.28),'Research Quality Score category']= 3
y4 = data.loc[(data['Research Quality Score']>69.28)& (data['Research Quality Score']<=79.2),'Research Quality Score category']= 4
y5 = data.loc[(data['Research Quality Score']>79.2)& (data['Research Quality Score']<=98.6),'Research Quality Score category']= 5

# f, ax = plt.subplots(1,2,figsize=(8,8))
# y6 = data[data['Research Quality Score category']==5]['location'].value_counts().head().plot.bar(ax=ax[0])
# y10 = ax[0].set_title('top 5 countries having high Research Quality Score universities')
# y7 = data['location'].value_counts().head().plot.bar(ax=ax[1])
# y11 = ax[1].set_title('top 5 countries in the rank list')
# plt.show()
#united states,uk and china has high number of universities having research quality score more than 79.2

y8 = pd.DataFrame(data[(data['location']=='India')].groupby(['Research Quality Score range'])['Research Quality Score range'].count())
print(y8)
y9 = data[data['location']=='India'].groupby(['location'])['location'].count().sum()
print(y9)
# sns.countplot(x= 'Research Quality Score range', data= data[data['location']=='India'])
# plt.show()
# z1 = data[data['location']=='India'].head(5).plot.bar(x='Name',y ='Research Quality Score')
# z2 = plt.xticks(rotation = 0, ha='center')
# plt.show()
#Amity university,Jamia milia islamia,and aligarh muslim university are top universities of india having high Research Quality Score.
#the total 15 indian universities , most of them got very less score in Research Quality.

z1 = data.groupby(['Name','Industry Score'],as_index=False)['Industry Score'].max().sort_values(by='Industry Score',ascending = False).head(15)
print(z1)
#  The University of Tokyo           100.0
#   University of California, San Diego           100.0
#  National Taiwan University (NTU)           100.0
#  City University of Hong Kong           100.0
#  Duke University           100.0
#  Nanyang Technological University, Singapore           100.0
#   The Hong Kong University of Science and Techno...           100.0
#  Seoul National University           100.0
#     Koç University           100.0
#   Stanford University           100.0
#  University of Erlangen-Nuremberg           100.0
#   KU Leuven           100.0
# z2 = data[data['location']=='India'].groupby(['Name','Industry Score'],as_index=False)['Industry Score'].max().sort_values(by='Industry Score',ascending = False).head(5)
# sns.barplot(x='Name',y='Industry Score',data = z2)
# print(z2)
# plt.show()    # india's top 5 universities having high industry score.
# Manipal Academy of Higher Education            66.4
#  Aligarh Muslim University            65.2
#  KIIT University            65.0
#  Panjab University            64.3
#  Jamia Millia Islamia            49.1


p = data.groupby(['Name','International Outlook'],as_index=False)['International Outlook'].max().sort_values(by='International Outlook',ascending = False).head(5)
print(p)
#   Name                               International Outlook
#   City University of Hong Kong                   99.0
#   University of Surrey                   98.1
#   University of Southampton                   98.1
#   Durham University                   98.0
#   University of Hong Kong                   97.6

# p1= data[data['location']=='India'].groupby(['Name','International Outlook'],as_index=False)['International Outlook'].max().sort_values(by='International Outlook',ascending = False).head(5)
# plt1 = sns.barplot(x='Name',y ='International Outlook',data= p1)
# plt.show()
#top 5 universities of India having high score in International Outlook.
#Lovely professional University
#UPES.
#Symbiosis International University.
#Aligarh Muslim University.
#Manipal Academy of Higher Education.

p3 = data.groupby(['Name','Research Environment Score'],as_index=False)['Research Environment Score'].max().sort_values(by='Research Environment Score',ascending = False).head(10)
print(p3)
#  University of Oxford                        97.4    #top 10 countries with best Research Environment.
#         Massachusetts Institute of Technology                        96.5
#       National University of Singapore                        95.9
#      Tsinghua University                        95.2
#              University of Cambridge                        94.6
#  London School of Economics and Political Science                        94.5
#         The University of Chicago                        93.5
#         Harvard University                        93.4
#           University of California, Berkeley                        92.7
#        Peking University                        91.8


# p4 = data[data['location']=='India'].groupby(['Name','Research Environment Score'],as_index=False)['Research Environment Score'].max().sort_values(by='Research Environment Score',ascending = False).head(5)
# plt1 = sns.barplot(x='Name',y ='Research Environment Score',data= p4)
# plt.show() #Top 5 universities of india which provide best Research Environment to their Students.
#University of Delhi
#Banaras University
#KIIT University
#Aligarh Muslim University
#Manipal Academy of Higher Education

print(data.columns)
# data.drop(['Name','location','Overall scores','Research Quality Score range','Research Quality Score category'],axis=1,inplace=True)
# i1 = data['Research Quality Score'] = data['Research Quality Score'].round().astype(int)
# i2 = data['Industry Score'] = data['Industry Score'].round().astype(int)
# i3 = data['International Outlook'] = data['International Outlook'].round().astype(int)
# i4 = data['Research Environment Score'] = data['Research Environment Score'].round().astype(int)
# i5 = data['Teaching Score'] = data['Teaching Score'].round().astype(int)
#
# plt4 = sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2,annot_kws={'size':20})
# plt.show()
#where there is good teaching there will be good research environment also.

# from sklearn.linear_model import LinearRegression
#
# random_number = np.random.randint(0,100)
# print(random_number)

print(data.columns)

o1 = data.groupby(['Name','rank','Teaching Score'],as_index=False)['Teaching Score'].max().sort_values(by='Teaching Score',ascending=False).head(5)
print(o1)
# Name                rank            Teaching Score
# Stanford University     2            98.2
# Peking University    10            96.3
# Yale University     9            96.1
# Massachusetts Institute of Technology     1            96.0
# Harvard University     3            95.0
# University of Cambridge     5            93.8
# University of Oxford     5            93.5
# Tsinghua University     8            93.2
# University of Pennsylvania    12            92.2
# Columbia University    14            92.0

o2= sns.barplot(x='Name',y='Teaching Score',data = o1)
o3 = o2.set_title('Name of the University VS Teaching Score')
plt.show()

import plotly.express as px
# plt1= px.scatter(data,y='Teaching Score',x = 'rank')
# plt1.show()
#it looks like some exponential decay graph

# plt2 = px.scatter(data,x='rank',y='Overall scores')
# plt2.show()

# plt3= px.scatter(data,x='rank',y='Industry Score')
# plt3.show()
#for the rank prediction, industry score might not be a good feature.

# plt4 = px.scatter(data,x='International Outlook',y='rank')
# plt4.show()

plt5 = px.scatter(data,x='Research Quality Score',y='rank')
plt5.show()
plt6= px.scatter(data,x='Research Environment Score',y='rank')
plt6.show()



