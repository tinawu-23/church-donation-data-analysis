#!/usr/bin/env python3
import os
import pandas as pd

# read initial parish csv file with missing urls
df = pd.read_csv('PA-Parishes-complete.csv')

# create new df
df_filterparish = df
df_filterparish['PDF'] = 'N'
df_filterparish['Bulletin'] = 'N'

# open two filter files
pdf_filter = open('pdf_filter.txt','r').read().splitlines()
bulletin_filter = open('bulletin_filter.txt','r').read().splitlines()

# fill in filter data
for i in range(df.shape[0]):
	try:
		site = str(df['URL'][i]).split('/')[2].replace('www.','')
	except:
		continue

	if site in pdf_filter:
		df_filterparish.at[i,'PDF']='Y'		
	if site in bulletin_filter:
		bulletinfilter = 'ls -r parish_docs/{} | grep bulletin | wc -l'.format(site)
		num = str(os.popen(bulletinfilter).read()).rstrip()
		df_filterparish.at[i,'Bulletin']=num

# export df as new csv file
df_filterparish.to_csv('PA-Parishes-filter.csv', encoding='utf-8', index=False)

