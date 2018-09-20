#!/usr/bin/env python3

import pandas as pd
from googlesearch import search 

# read initial parish csv file with missing urls
df = pd.read_csv('PA-Parishes.csv', nrows=20)
df_church = df['Church']
df_city = df['City']

# create new df
df_urlComplete = df

# fill in urls using googlesearch
for i in range(df.shape[0]):
	if df['URL'][i]!='None':
		continue
	querystr = df_church[i] + " " + df_city[i]
	for site in search(querystr, tld="com", num=3, stop=1, pause=2):
		if 'facebook' not in site and 'wikipedia' not in site:
			df_urlComplete.loc['URL',i]=site
			break

# export df as new csv file
df_urlComplete.to_csv('PA-Parishes-complete.csv', encoding='utf-8', index=False)

