#!/usr/bin/python2
# -*- coding: utf-8 -*

__author__ = 'David Ureba'

import twitter

# Auth function
def oauth_login():
	CONSUMER_KEY 	   = ''
	CONSUMER_SECRET	   = ''
	OAUTH_TOKEN 	   = ''
	OAUTH_TOKEN_SECRET = ''
	auth 			   = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	return twitter.Twitter(auth=auth)