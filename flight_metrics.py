#This script gives an in-depth look at flight arrivals to any worldwide airport via the website FlightAware.com (using web scraping) 

#import libraries
import pandas as pd 
import numpy as np 
import requests 
from bs4 import BeautifulSoup
import math 
import re 
import altair as alt 
from datetime import datetime 
from dateutil import parser
import dateutil.parser
import altair_viewer
import scipy.stats as stats
import seaborn as sns 
import plotly.graph_objects as go
import datetime 
import time 

#set airport parameters (airport code and airport name)
air_code='KSAN'
airport_name='San Diego'

#scrape webpages from flightaware.com
#page 1 
##############################
page=20
url="https://flightaware.com/live/airport/{}/arrivals?;offset=20;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

#export list to csv 
df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df1.csv")

#page 2 
##############################
page=40
url="https://flightaware.com/live/airport/{}/arrivals?;offset=40;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

#export lists to csv (cali jungles/cannabis?)
df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df2.csv")

########page 3 
page=60
url="https://flightaware.com/live/airport/{}/arrivals?;offset=60;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df3.csv")

#####page 4 
page=80
url="https://flightaware.com/live/airport/{}/arrivals?;offset=80;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df4.csv")

#########page 5 
page=100 
url="https://flightaware.com/live/airport/{}/arrivals?;offset=100;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df5.csv")

######### page 6 
page=120
url="https://flightaware.com/live/airport/{}/arrivals?;offset=120;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)

df.to_csv("df6.csv")

##############page 7 
page=140
url="https://flightaware.com/live/airport/{}/arrivals?;offset=140;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df7.csv")


##############page 8 
page=160
url="https://flightaware.com/live/airport/{}/arrivals?;offset=160;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df8.csv")

##############page 9 
page=180
url="https://flightaware.com/live/airport/{}/arrivals?;offset=180;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df9.csv")

##############page 10
page=200
url="https://flightaware.com/live/airport/{}/arrivals?;offset=200;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df10.csv")

##############page 11
page=220
url="https://flightaware.com/live/airport/{}/arrivals?;offset=220;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df11.csv")

##############page 12
page=240
url="https://flightaware.com/live/airport/{}/arrivals?;offset=240;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df12.csv")

##############page 13
page=260
url="https://flightaware.com/live/airport/{}/arrivals?;offset=260;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df13.csv")

##############page 14
page=280
url="https://flightaware.com/live/airport/{}/arrivals?;offset=280;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df14.csv")

##############page 15
page=300
url="https://flightaware.com/live/airport/{}/arrivals?;offset=300;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df15.csv")

##############page 16
page=320
url="https://flightaware.com/live/airport/{}/arrivals?;offset=320;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df16.csv")

##############page 17
page=340
url="https://flightaware.com/live/airport/{}/arrivals?;offset=340;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df17.csv")

##############page 18
page=360
url="https://flightaware.com/live/airport/{}/arrivals?;offset=360;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df18.csv")

##############
page=380
url="https://flightaware.com/live/airport/{}/arrivals?;offset=380;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df19.csv")

##############
page=400
url="https://flightaware.com/live/airport/{}/arrivals?;offset=400;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df20.csv")

##############
page=420
url="https://flightaware.com/live/airport/{}/arrivals?;offset=420;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df21.csv")

##############
page=440
url="https://flightaware.com/live/airport/{}/arrivals?;offset=440;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df22.csv")

##############
page=460
url="https://flightaware.com/live/airport/{}/arrivals?;offset=460;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df23.csv")

##############
page=480
url="https://flightaware.com/live/airport/{}/arrivals?;offset=480;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df24.csv")

##############
page=500
url="https://flightaware.com/live/airport/{}/arrivals?;offset=500;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df25.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=520;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df26.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=540;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df27.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=560;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df28.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=580;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df29.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=600;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df30.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df31.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=620;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df32.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=640;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df33.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=660;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df34.csv")


###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=640;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df33.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=680;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df35.csv")

url="https://flightaware.com/live/airport/{}/arrivals?;offset=700;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df36.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=700;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df37.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=720;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df38.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=740;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df39.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=760;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df40.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=780;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df41.csv")

###############
url="https://flightaware.com/live/airport/{}/arrivals?;offset=800;order=actualarrivaltime;sort=DESC".format(air_code)
page=requests.get(url)
soup=BeautifulSoup(page.content)
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))

flights20=[]
for f in soup_div1:
    print(f.get_text()) 
    flights20.append(f.get_text())

flights1_20=[]
for f in soup_div2:
    print(f.get_text()) 
    flights1_20.append(f.get_text())

flights_all_20=flights20+flights1_20 

df=pd.DataFrame({'col':flights_all_20})
rows_df=df.shape[0]/5
rows_df=math.floor(rows_df)
df=df.values.reshape(rows_df,5)
df=pd.DataFrame(df)
df.to_csv("df42.csv")


#concatenate the csv file (airport arrivals)  
filenames1=['df1.csv','df2.csv','df3.csv','df4.csv','df5.csv','df6.csv',
        'df7.csv','df8.csv','df9.csv','df10.csv','df11.csv','df12.csv',
        'df13.csv','df14.csv','df15.csv','df16.csv',
        'df17.csv','df18.csv','df19.csv','df20.csv',
        'df21.csv','df22.csv','df23.csv','df24.csv',
        'df25.csv','df26.csv','df27.csv','df28.csv','df29.csv',
        'df30.csv','df31.csv','df32.csv','df33.csv',
        'df35.csv','df36.csv','df37.csv','df38.csv','df39.csv',
        'df40.csv','df41.csv','df42.csv']

#clean the dataset (airport arrivals)
to1=pd.concat([pd.read_csv(f) for f in filenames1])
to1.columns=['unnamed','flight_no','aircraft','dep','dep_time','arr_time']
to1=to1.drop_duplicates(['dep','flight_no','arr_time'],keep='last') #drop duplicate flights 
to1=to1[~to1['dep'].str.contains(air_code,na=False)] #remove the same departure as the arrival airport 

#departure counts
dep_cnts=to1.dep.value_counts()
dep_cnts=pd.DataFrame(dep_cnts)
dep_cnts.reset_index(level=0,inplace=True)
dep_cnts['pct']=dep_cnts.dep/dep_cnts.dep.sum()
dep_cnts['pct']=round(dep_cnts.pct,3)*100
dep_cnts.columns=['city','count','percent']

#set departure counts threshold 
dep_cnts1=dep_cnts[dep_cnts.percent>=1.5]
dep_cnts1['city']=dep_cnts1.city.str.split('(').str[0]

#departure counts to csv
dep_cnts.to_csv("dep_cnts.csv")

#viz1
f1xx=alt.Chart(dep_cnts1).mark_bar().encode(
    x='city',
    y='percent',
    color='city'
).properties(height=300,width=250,title="Most Frequent Cities Arriving at " + airport_name)
altair_viewer.show(f1xx)

#ii.florida flag
fla=to1[to1.dep.str.contains('KFLL|KRSW|KJAX|KEYW|KMLB|KMCO|KPNS|KTLH|KTPA|KPBI')]
pct_fla=(fla.shape[0]/to1.shape[0])*100
pct_fla=round(pct_fla,2)

#U.S. flights flag (busy international airports)
bus_air=to1[to1.dep.str.contains('KMIA|KLAX|KSFO|kEWR|KORD|kATL|KIAH|KFLL|KDFW')]
bus_air1=bus_air.dep.value_counts()
bus_cnts=pd.DataFrame(bus_air1)
bus_cnts.reset_index(level=0,inplace=True)
bus_cnts['pct']=bus_cnts.dep/bus_cnts.dep.sum()
bus_cnts['pct']=round(bus_cnts.pct,3)*100
bus_cnts.columns=['city','count','percent']

f2x=alt.Chart(bus_cnts).mark_bar().encode(
    x='city',
    y="percent"
).properties(height=300,width=250,title="Busy U.S. Airports Flying To " + airport_name)
altair_viewer.show(f2x)


#international cities(top 35 airports for air traffic) 
int_spike=to1[to1.dep.str.contains('ZBAA|OMDB|EGLL|ZSPD|LFPG|KMIA|KLAX|RJTT|KORD|KDFW|EHAM|VHHH|RKSI|EDDF|KDEN|VIDP|WSSS|VTBS|KJFK|WMKK|LEMD|KSFO|ZUUU|WIII|ZGSZ|LEBL|LTFM|KSEA|KLAS|KMCO|CYYZ|MMMX|KCLT|UUEE')]
pct_int=int_spike.shape[0]/to1.shape[0]
pct_int=round(pct_int*100,2)

pi=int_spike.dep.value_counts()
pi=pd.DataFrame(pi)
pi.reset_index(level=0,inplace=True)
pi.columns=['city','count']
busy_air=pi['city'].iloc[0]

f3x=alt.Chart(pi).mark_bar().encode(
    x='city',
    y="count"
).properties(height=300,width=250,title="One of Busiest International Hubs Flying Into " + airport_name + " is " + busy_air)
altair_viewer.show(f3x)

#percent departing from xx city (AM vs. PM)
am=to1[to1.dep_time.str.contains('AM',na=False)]
pm=to1[to1.dep_time.str.contains('PM',na=False)]

#count AM and PM departure points 
ac=am.dep.value_counts()
ac=pd.DataFrame(ac)
ac.reset_index(level=0,inplace=True)
ac.columns=['city','cnt_am']

pm1=pm.dep.value_counts()
pm1=pd.DataFrame(pm1)
pm1.reset_index(level=0,inplace=True)
pm1.columns=['city','cnt_pm']

amF=pd.merge(ac,pm1,on="city")
amF['pct_pm']=(amF.cnt_pm/(amF.cnt_pm+amF.cnt_am))*100
amF['pct_pm']=round(amF['pct_pm'],1)
med_pm_flights=amF.cnt_pm.quantile(0.99)
amF=amF[amF.pct_pm>=med_pm_flights]
amF=amF[["city","pct_pm"]][0:20]
amF.columns=["city","pct_pm_dep"]
amF=amF.sort_values(by="pct_pm_dep",ascending=False)
amF.columns=['city','percent']

fig_pm = go.Figure(data=[go.Table(
    header=dict(values=list(amF.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[amF.city,amF.percent],
               fill_color='white',
               align='left'))
])

fig_pm.update_layout(
    height=800,
    showlegend=False,
    title_text="Percent of Afternoon and Evening Departures For Popular Flights To " +  airport_name ,
)

fig_pm.show() 

#median flight time for airports min >=1.5% of all flights 
to2=to1 
to2['est_arr_time1']=to2['arr_time'].str.strip().str[4:9]
to2['dep_time1']=to2['dep_time'].str.strip().str[4:9]
to2['zero_one_dep']=to2.dep_time1.str.strip().str[:1]
to2['zero_one_arr']=to2.est_arr_time1.str.strip().str[:1]
to2['dt_dep']=to2['dep_time'].apply(dateutil.parser.parse)
to2['dt_dep']=pd.to_datetime(to2['dt_dep'],utc=True) #convert departure time to time utc 

#difference in takeoffs by origin, aircraft, flight_no 
to2a=to2.sort_values(by=['dep','dt_dep'])
to2a['time_dep'] = pd.to_datetime(to2a.dt_dep).dt.tz_localize(None)
to2a['time_dep']=pd.to_datetime(to2a.time_dep)
to2a=to2a.sort_values(by=["dep","time_dep"]) #sort by dep, time_dep 
to2a['dep_time_diff']=to2a['time_dep'].diff()
to2a['dep_time_diff']=to2a['dep_time_diff'].dt.total_seconds()
to2a[["dep","time_dep","dep_time_diff"]][150:185]

#median dep time difference by departure point 
xx=to2a
xx=xx[xx.dep_time_diff>=0]
dep_med=xx.groupby('dep')['dep_time_diff'].median() 
dep_med=pd.DataFrame(dep_med)
dep_med.reset_index(level=0,inplace=True)
dep_med['min_diff']=dep_med.dep_time_diff/60 
dep_med.columns=['city','sec_diff','min_diff']

#merge with departure counts (percent >=1.5% of all flights, median flight diff)
dep_med1=pd.merge(dep_cnts,dep_med,on="city")
dep_med1=dep_med1[dep_med1.percent>=1.5]
dep_med1=dep_med1.sort_values(by="min_diff")
dep_med1['city']=dep_med1.city.str.split('(').str[0]
dep_med2=dep_med1[dep_med1.min_diff !=0]
dep_med2=dep_med2[["city","percent","min_diff"]]
dep_med2['percent']=round(dep_med2['percent'],3)
dep_med3=dep_med1[["city","percent"]]
dep_med3=dep_med3.sort_values(by="percent",ascending=False)

#to a table format (median minutes between takoffs) 
f1= go.Figure(data=[go.Table(
    header=dict(values=list(dep_med2.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[dep_med2['city'], dep_med2['percent'],dep_med2['min_diff']],
               fill_color='white',
               align='left')) ])

f1.update_layout(
    height=1000,
    showlegend=False,
    title_text="Most Popular Flights Arriving to " +  airport_name  + " and the Median Minutes Between Departures",
)            
f1.show()

#most frequent flight numbers
fl_no=to2.flight_no.value_counts()
fl_no=pd.DataFrame(fl_no)
fl_no.reset_index(level=0,inplace=True)
fl_no.columns=['flight_no','count']
fl_no=fl_no[fl_no['count']>=5]
fl_no_list=fl_no['flight_no'].tolist()
fl_no_list 

#cities with flight numbers (minimum 5 flights) 
fl_no1=to2[to2.flight_no.isin(fl_no_list)]
cities1=fl_no1.drop_duplicates(subset=['dep','arr_time'],keep="last")
cities1=cities1[["flight_no","dep","dep_time","arr_time"]]

fl_noX=pd.merge(fl_no,cities1,on="flight_no")
fl_noX=fl_noX.drop_duplicates(subset=['dep','flight_no'],keep="first")
fl_noX=fl_noX[['flight_no','dep', 'dep_time', 'arr_time']]
fl_noX.columns=['flight_no','city','dep_time','arr_time']

fig1 = go.Figure(data=[go.Table(
    header=dict(values=list(fl_noX.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[fl_noX.flight_no,fl_noX.city,fl_noX.dep_time,fl_noX.arr_time],
               fill_color='white',
               align='left'))
])

fig1.update_layout(
    height=800,
    showlegend=False,
    title_text="Most Recent Popular Flight Number Routes Arriving to " +  airport_name ,
)

fig1.show()

#most recent flights (top 25)
rec_fl=to2.iloc[0:25]
rec_fl=rec_fl[['flight_no','dep', 'dep_time', 'arr_time']]
fig2xxx = go.Figure(data=[go.Table(
    header=dict(values=list(rec_fl.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[rec_fl.flight_no,rec_fl.dep,rec_fl.dep_time,rec_fl.arr_time],
               fill_color='white',
               align='left'))
])

fig2xxx.update_layout(
    height=800,
    showlegend=False,
    title_text="Recent Flights Arriving to " +  airport_name ,
)

fig2xxx.show()

#percent international vs. domestic flights 
inter=to2[~to2.dep.str.contains('K',na=False)] #filter out non-domestic departures 
dom=to2[to2.dep.str.contains('K',na=False)]
dom=dom[~dom.dep.str.contains('BOG|STT|MDE|MKJP|SKCL|SYPE|MKJS|SKCG|BAQ|TXKF')]

#estiamte of domestic vs. international flights 
pct_dom=dom.shape[0]/(dom.shape[0]+inter.shape[0])
pct_dom=round(pct_dom,3)*100
print(pct_dom)

#airline counts (most popular and least popular)
to2['air']=to2['flight_no'].str[:4]
ac=to2.air.value_counts()
ac=pd.DataFrame(ac)
ac.reset_index(level=0,inplace=True)
ac.columns=['airline','count']
ac['pct']=ac['count']/(ac['count'].sum())
ac['pct']=round((ac.pct*100),1)

fl_ac=ac[ac.pct>=1.5]
y_pos = np.arange(len(fl_ac))
pct_arrivals=fl_ac.pct.tolist()
cities=fl_ac.airline.tolist()

fig_air=plt.figure()
plt.bar(y_pos, pct_arrivals, align='center', alpha=0.5)
plt.xticks(y_pos, cities) 
plt.ylabel('percent of all arrivals')
plt.xlabel('')
plt.title('Popular Airlines Landing in ' + airport_name)
plt.savefig('arrivals_city.png')

