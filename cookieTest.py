#!/usr/bin/env python
# encoding: utf-8
"""
cookieTest.py

Created by Jonathan Dalrymple on 2008-06-20.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import cookielib
import urllib2
import pickle

class FBCookieJar( cookielib.CookieJar ):
	def __init__( self ):
		cookielib.CookieJar.__init__( self )
	#Serialize the object
	def serialize(self, file ):
		import pickle
		
		retVal = False
		
		#Now that all cookies have been added serialize the object
		if file:
			pickle.dump( self._cookies, file )
			retVal = True
		else:
			retVal = pickle.dumps( self._cookies )
		
		#Should this even have a return statement
		return retVal
	
	#Input can be either a file of string
	def loadSerialized( self, serializedArrOrFile ):
		import pickle
		import types
		import copy
		
		#is String
		if type(serializedArrOrFile) == types.StringTypes:
			tempArr = pickle.loads( serializedArrOrFile )
						
		#If we're dealing with a file
		elif type(serializedArrOrFile) == types.FileType:
			tempArr = pickle.load( serializedArrOrFile )
				
		if type(tempArr) != types.DictType:
			raise TypeError, 'Serialized Object is not a list object'
			
		#I didn't like this, but i was left with few choices given the fact
		#that the FileCookieJar object took the filename instead of a file object which
		#could have been subclassed
		
		#Thanks to OSS i have the implementation details
		#Get the lock
		self._cookies_lock.acquire()
		
		#Clear the array
		self._cookies = {}
		#Internal cookies array
		
		#self._cookies = tempArr
		self._cookies = copy.deepcopy( tempArr )
		
		#Release the lock
		self._cookies_lock.release()
		
		
def main():
	#cookieJar = FBCookieJar() #cookielib.CookieJar()
	#browser = urllib2.build_opener( urllib2.HTTPCookieProcessor( cookieJar ) )
	
	#x = browser.open( 'http://localhost:8888/cookie.php' )
	
	#x = browser.open('http://www.google.com')
	
	#print '='*5 + 'Serializing cookies'
	#fh = open('cookies.dat','w')
	
	#cookieJar.serialize( fh )
	
	#fh.close
	
	#fh = None
	
	

	newCookieJar = FBCookieJar()
	print '='*5 +'Loading cookies in to jar'
	fh = open('cookies.dat','r')
	
	newCookieJar.loadSerialized( fh )
	
	print type(newCookieJar)
	
	for x in newCookieJar:
		print x

if __name__ == '__main__':
	main()

