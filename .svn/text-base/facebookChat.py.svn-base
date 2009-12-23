#!/usr/bin/env python
# encoding: utf-8
"""
facebookChat.py

Created by Jonathan Dalrymple on 2008-06-17.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import cookielib
import urllib
import urllib2

import re
import demjson
import random
import time
import types
import hashlib
import logging
import logging.config
from htmllib import HTMLParser

#My stuff
import fbcookiejar
import netabstraction
import serializabledict
import htmlextractor


#Setup the logging
logging.config.fileConfig("logging.conf")

log = logging.getLogger("Facebook Chat")

try:
	import Growl
except ImportError:
	log.warn('Growl not found')

def notifyViaGrowl( username ):
	note = Growl.GrowlNotifier( applicationName = 'Facebook Chat', 
								notifications = ['Buddy Online']
	)
	
	note.register()
	
	note.notify(
		noteType = 'Buddy Online',
		title = '%s is facebook' % username,
		description = '%s is currently online' % username
	)
	
	
#This is where the magic happens
class FacebookChat():

	def __init__(self):
		self.loginURL = 'https://login.facebook.com/login.php'
		self.tx = '/ajax/chat/send.php'
		self.buddyList = '/ajax/presence/update.php'
		
		#Persistent Data stoer
		self._dataStore = serializabledict.SerializableDictionary('Key')

		
		self.cookieJar = fbcookiejar.FBCookieJar()
		self.browser = None
		
		#Generate a unique GUID for this
		#self._guid = 
	
	#Deals with the issue of serialization and concurrency
	#def getGUID():
	#	return self._guid
	
	#Called at the end of each function
	def pack( self ):
		log.info( 'packing...' )
		
		#Save the info to the data files
		fh = open('cookies.dat','w')
		self.cookieJar.serialize( fh )
		fh.close()
		fh = None
		
		fh = open('facebookTemp.dat','w')
		self._dataStore.serializeToFile( fh )
		fh.close()
		fh = None
		
	#Called at the begin of each function
	def unpack( self ):
		log.info( 'Unpacking...' )
		
		try:
			fh = open('cookies.dat','r')
			self.cookieJar.loadSerialized( fh )
			fh.close()
			fh = None
	
			fh = open('facebookTemp.dat','r')
			self._dataStore.loadFromFile( fh )
			fh.close()
			fh = None
		except IOError, e:
			print 'Error in Unpack method: %s' % e
		
	def _genConnectionURL(self, seq=-1,channel='01'):
		
		#Generate random strings
		rand = random.randint( 1, 99 )
		
		rand2 = str(time.time())
		
		rand2 = rand2[0:len(rand2)-3]
		
		retStr = 'http://0.channel%s.facebook.com/x/%s/true/p_%s=%d' % ( channel, rand2, self._dataStore['userId'], seq )
		
		return retStr
		
		
	def login(self, email, password ):
		#Unserialize any and all objects
		#self.unpack()
		
		#Do i really need to unserialize data here?
		#Considering that i'm going to overwrite at the end of this method
		
		self.browser = urllib2.build_opener( urllib2.HTTPCookieProcessor( self.cookieJar ) )
		
		#facebook sets a cookie on the first page, and checks the value on the next
		#To make it happy we have to pretent to be a user 
		x = self.browser.open( self.loginURL )
		
		log.info('Logging in via %s', x.geturl() )
		
		x = self.browser.open( self.loginURL, 'email=%s&pass=%s&' % (email, password) )
		
		log.info( x.geturl() )
		#x is a request object	
		
		log.info( 'Parsing HTML' )
		
		html = htmlextractor.HTMLExtractor(0)
		
		content = x.read()
		
		html.feed( content )
		
		html.close()
		
		self._dataStore['userId'] = re.compile('[0-9]+$').search( html.linkStr ).group()
		
		log.info( 'Facebook id is %s', self._dataStore['userId'] )
		
		#Save to the persistent data store
		self._dataStore['postFormId'] = html.postFormId
		
		#Now that login is complete, we can pack for next time
		self.pack()
	
	def getBuddyList( self ):
		
		self.unpack()
		
		self.browser = urllib2.build_opener( urllib2.HTTPCookieProcessor( self.cookieJar ) )
		
		log.info('Getting Buddy list')
		
		args = {
			'buddy_list':'1',
			'force_render': 'true',
			'popped_out': 'false',
			'post_form_id': self._dataStore['postFormId'],
			'user': self._dataStore['userId']
		}
		
		argsStr = str()
		
		for arg in args.items():
			argsStr += '%s=%s&' % (arg[0], arg[1])
		
		#x = self.browser.open('http://www.facebook.com/ajax/presence/update.php?buddy_list=1', argsStr )
		
		x = self.browser.open('http://www.facebook.com/ajax/chat/buddy_list.php', argsStr )
		log.info( x.geturl() )
		
		log.info('Reading Contents')
		
		#save the json response to a file for debugging

		pseudoInvalidJSON = x.read()
		
		validJSON = pseudoInvalidJSON[9:len(pseudoInvalidJSON)]
		
		JSONObj = demjson.decode( validJSON )
		
		log.info('Buddylist')
		
		#print JSONObj
		
		#Handle Error
		if JSONObj['error'] != 0:
			
			log.error('Buddylist retreival failed: %s' % JSONObj['errorDescription'] )
		
		else:
			log.info( 'Buddys available %d' % JSONObj['payload']['buddy_list']['availableCount'] )
		
			for buddyId in JSONObj['payload']['buddy_list']['nowAvailableList']:
				
				buddyName = JSONObj['payload']['buddy_list']['userInfos'][buddyId]['name']
				
				print "%s is Online : %s" % (buddyName , buddyId) 
				
				notifyViaGrowl( buddyName )
				
			log.info('Buddy list Retrieval Complete')
		
		
		
		self.pack()
		
	def send( self, recipient ):
		
		self.unpack()		
		args = {
			'msg_text':'Im trying something out, please ignore me ^_^, u know like usually',
			'to': recipient,
			'msg_id': random.randint( 1, 9999999 ),
			'client_time': round(time.time()*1000),
			'post_form_id' : self._dataStore['postFormId']
		}
		
		argsStr = str()
		
		for arg in args.items():
			argsStr += '%s=%s&' % (arg[0], arg[1])
				
		x = self.browser.open('http://www.facebook.com/ajax/chat/send.php', argsStr )
		self.pack()
		
	def listen( self):
		
		self.unpack()
		
		msgReceived = False
		
		log.info( self._genConnectionURL() )
		x = self.browser.open( self._genConnectionURL() )

		log.info( 'Connected to: %s' % x.geturl() )
		
		pseudoInvalidJSON = x.read()
		validJSON = pseudoInvalidJSON[9:len(pseudoInvalidJSON)] 
		
		JSONObj = demjson.decode( validJSON )
		print JSONObj
		
		if JSONObj['t'] == 'refresh':
			seqNo = 0
			
			x = self.browser.open( self._genConnectionURL( seqNo ) )
			
			log.info( 'Getting %s', x.geturl())
			
			pseudoInvalidJSON = x.read()
			
			validJSON = pseudoInvalidJSON[9:len(pseudoInvalidJSON)]
			
			JSONObj = demjson.decode( validJSON )
			
			print JSONObj
			
			while( JSONObj['t'] == 'continue' ):
				x = self.browser.open( self.genConnectionURL( seqNo ) )
				
				pseudoInvalidJSON = x.read()
				
				validJSON = pseudoInvalidJSON[9:len(pseudoInvalidJSON)]
				
				JSONObj = demjson.decode( validJSON )
				
				if JSONObj['t'] == 'msg':
					console.log('Message Recieved!')
					print JSONObj
					msgReceived = True 	
		
		self.pack()
		
		
def main():
	
	fb = FacebookChat()
	
	doLogin = raw_input('Login? (y/n)')
	
	if doLogin == 'y':	
		#Login into facebook
		fb.login('veritech19@gmail.com','robotech')
	
	#Get the buddy list
	fb.getBuddyList()
	
	fb.listen()
	

if __name__ == '__main__':
	main()

