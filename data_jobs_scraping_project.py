#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd


# In[2]:


# Getting URL of the website

url = 'https://wuzzuf.net/search/jobs/?q=data%20analysis&a=hpb'
data = urlopen(url)
html = data.read()
data.close()


# In[3]:


# Creating a container for our data

soup = bs(html, 'html.parser')
container = soup.find_all('div', {'class':'css-1gatmva e1v1l3u10'})


# In[4]:


# Checking data and our access

job_title = container[0].find_all('h2', {'class':'css-m604qf'})
print(job_title[0].text.strip())

company = container[0].find_all('a', {'class':'css-17s97q8'})
print(company[0].text.strip())

job_type = container[0].find_all('div',{'class':'css-1lh32fc'})
print(job_type[0].text.strip())


# In[5]:


# Creating a file to store our data

f = open('data_analysis_jobs.csv', 'w')

header = 'job_title, company, job_type\n'
f.write(header)

for x in container:
    job_title = x.find_all('h2', {'class':'css-m604qf'})
    job_title = job_title[0].text.strip()
    
    company = x.find_all('a', {'class':'css-17s97q8'})
    company = company[0].text.strip()
    
    job_type = x.find_all('div',{'class':'css-1lh32fc'})
    job_type = job_type[0].text.strip()
    
    f.write(job_title + ', ' + company + ', ' + job_type + '\n')

f.close()


# In[6]:


# Creating pandas DataFrame

pd.read_csv('data_analysis_jobs.csv')

