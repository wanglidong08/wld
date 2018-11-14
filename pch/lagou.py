#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import time

import requests
import pandas as pd
from pymongo import MongoClient

def GetData(url,i):
	h={
	'Cookie':'_ga=GA1.2.447025000.1542122812; user_trace_token=20181113232652-8bbf95fc-e758-11e8-88ab-5254005c3644; LGUID=20181113232652-8bbf99a5-e758-11e8-88ab-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFCAAEG52631EB0ACBB6FD4311F0F5DD02DF4C3; TG-TRACK-CODE=index_search; LGRID=20181114132154-3331d211-e7cd-11e8-88ae-5254005c3644; SEARCH_ID=4aecbb5f138d4feabc9c0f62e7c86fe5',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
	'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
	}
	payload=(
	{'first': 'true',
	'pn': i,
	'kd': '爬虫'})
	print(payload)
	r=requests.post(url,data=payload,headers=h)
	print(r.status_code)
	data=r.json()['content']['positionResult']['result']
	print ('first')
	return data


def LoadData(data):

	client=MongoClient()
	db=client.lagou
	lagou_set=db.set
	lagou_set.insert_many(data)
	print('second')

if __name__=='__main__':
	url1='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
	for i in range(1,27):
		data1=GetData(url1,i)
		LoadData(data1)
		time.sleep(5)
	print('the end')