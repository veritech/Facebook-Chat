#!/usr/bin/env python
# encoding: utf-8
"""
FBCookieJar.py

Created by Jonathan Dalrymple on 2008-06-21.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import cookielib
import urllib2
import pickle

class FBCookieJar( cookielib.CookieJar ):

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
		


