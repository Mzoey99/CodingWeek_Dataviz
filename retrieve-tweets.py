#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Retrieve tweets from an id list

@author : j. lark
'''

import os
import codecs
import argparse
from twython import Twython, exceptions
import time
import json

parser = argparse.ArgumentParser()
parser.add_argument('config', help='Twitter API authentification configuration')
parser.add_argument('id_list_file', help='the file where tweets ids are stored (1 id per line)')
parser.add_argument('outputpath', help='the output dir where tweets are stored')
args = parser.parse_args()

def parse_config(configfile):
	config = {}
	fin    = codecs.open(configfile, 'r', 'utf-8')
	try:
		for line in fin:
			config[line.split(':')[0]] = line.split(':')[1].strip()
		fin.close()
	except:
		print('Configuration parameters are wrong, should be in a file of the form:\
		\nconsumer_key:your_consumer_key\
		\nconsumer_secret:your_consumer_secret\
		\naccess_token:your_access_token\
		\naccess_token_secret:your_access_token_secret')
		exit()
	return config

def main():
	config  = parse_config(args.config)
	twitter = Twython(config['consumer_key'], config['consumer_secret'], config['access_token'], config['access_token_secret'])
	if os.path.isdir(args.outputpath):
		fin = codecs.open(args.id_list_file, 'r', 'utf-8')
		i = 20
		for tweetid in fin:
			if i %900 == 0:
				time.sleep(60*61)
			tweetid = tweetid.strip()
			i +=1
			print(tweetid)
			if not (tweetid + '.txt') in os.listdir(args.outputpath):
				try:
					tweet = twitter.show_status(id=tweetid, expansions="author_id")
					fout  = codecs.open(tweetid + '.json', 'w', 'utf-8')
					fout.write(json.dumps({"text": tweet['text'],
						"date": tweet["created_at"],
						"auteur": tweet["user"]["name"],
						"localisation": tweet["user"]["location"]}))
					fout.close()
				except exceptions.TwythonError:
					pass
				
		fin.close()
	else:
		print ('The output directory does not exist !')
		exit()

if __name__ == '__main__':
	main()