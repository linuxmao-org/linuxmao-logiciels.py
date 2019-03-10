#!/usr/bin/python3

import sqlite3
from urllib.parse import urlparse
import requests
import argparse
import sys
import configparser

# read configuration file
config = configparser.ConfigParser()
config.read('linuxmao-logiciels.ini')
github_user = config['github']['github_user']
github_pass = config['github']['github_pass']

# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--logiciel", help="chercher si  une logiciel est présent dans la base de données locale")
parser.add_argument("--repo", help="chercher les maj dans les repos en ligne (repo = sourceforge, github, ALL)")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

# Connect to the sqllite DB
conn = sqlite3.connect('software.db')
c = conn.cursor()

# get latest release from github
def get_github_latest():

	c.execute("SELECT name,latest,url FROM software WHERE orig='github'")

	for row in c.fetchall():
		name = row[0]
		current_release = row[1]
		url = row[2]
		print (''+name+' - '+current_release+' - '+url+'')
		# parse the URL and extract the path
		o = urlparse(url)
		# generate the url to query github API and query it
		latest_url='https://api.github.com/repos'+o.path+'releases/latest'
		#print ('Latest release URL: '+latest_url)
		r = requests.get(latest_url, auth=(github_user, github_pass))
		# get the latest release
		latest_release = r.json()['tag_name']
		if current_release !=  latest_release: 
			print ("New release available : " +latest_release+ ' / URL: '+url+'releases/')
		print ("---")

# get latest release from sourceforge
def get_sourceforge_latest():

	c.execute("SELECT name,latest,url FROM software WHERE orig='sourceforge'")

	for row in c.fetchall():
		name = row[0]
		current_release = row[1]
		url = row[2]
		print (''+name+' - '+current_release+' - '+url+'')
		latest_url='https://sourceforge.net/projects/'+name+'/best_release.json'
		#print ('Latest release URL: '+latest_url)
		r = requests.get(latest_url)
		r.json()
		# get the latest release
		latest_release = r.json()['platform_releases']['linux']['filename']
		if current_release !=  latest_release: 
			print ("New release available : " +latest_release)
		print ("---")

# Look if the software is in the DB
def get_software_in_db(str):
	
	c.execute ("SELECT name,latest,url FROM software WHERE name LIKE ?",  ('%{}%'.format(str),))

	for row in c.fetchall():
		name = row[0]
		current_release = row[1]
		url = row[2]
		print (''+name+' - '+current_release+' - '+url+'')
	

if args.logiciel:
	get_software_in_db(str = args.logiciel)
elif args.repo == 'github':
	get_github_latest()
elif args.repo == 'sourceforge':
	get_sourceforge_latest()
elif args.repo == 'ALL':
	get_github_latest()
	get_sourceforge_latest()