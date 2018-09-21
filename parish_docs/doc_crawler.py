#!/usr/bin/env python3

import os
import pandas as pd
import multiprocessing as mp

def crawl(website):
	if 'www.' in website:
		website = website.replace('www.','')
	os.system("wget -r -x -w 1 -t 1 -l 3 -T 5 -nc -R jpg,jpeg,gif,png,tif,ppt,pptx,mp3,mpeg,css,js -U ResearchCrawler_tweninge@nd.edu {}".format(website))

if __name__ == '__main__':
	df = pd.read_csv('PA-Parishes-complete.csv', usecols=['URL'])
	p = mp.Pool(processes = 20)
	p.map(crawl,df['URL'])

