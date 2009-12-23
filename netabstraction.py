#!/usr/bin/env python
# encoding: utf-8
"""
netabstraction.py

Created by Jonathan Dalrymple on 2008-06-22.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import urllib2
import cookielib

try:
	from google.appengine.api import urlfetch
except ImportError:
	print "Couldn't find find google appengine"
	

#This acts as a abstraction from the default connection object
class FRHTTPResponse(object):
	def __init__( self, body = None, headers = {} ):
		self._body = body
		self._headersDict = headers
		
	def body( self ):
		return self._body
		
	def header( self, title=None ):
		return self._headersDict[title]
		
	def getCookies( self ):
		pass

class FRHTTPRequest(object):
	"""Abstraction of HTTP requests"""
	#import google.appengine.api.urlfetch
	
	def __init__( self, mode ):
		self.mode = mode
		self.cookieJar = cookielib.CookieJar()

	#perform get request
	def get( self, URL, ARGS = None ):
		
		if self.mode == 'googelappengine':
		
			urlfetch.fetch( URL, None, 'GET', False )
			
		elif self.mode == 'urllib2':
		
			req = urllib2.build_opener( urllib2.HTTPCookieProcessor( self.cookieJar ) )
			
			res = req.open( URL )
			
			headers = str(res.info()).split( "\r\n" )
			
			headerDict = {}
			
			#If i parse out the header names
			#namePattern = re.compile('^\w+?(.\w+):')
			headerPattern = re.compile(':\s')
			
			for header in headers:
				
				if len(header) > 0:
					s = headerPattern.split( header, 1 )
					
					headerDict[s[0].lower()] = s[1]

			#Create Response object
			#ret = FRHTTPResponse( res.read(), headerDict )
			#return ret
			return FRHTTPResponse( res.read(), headerDict )
			
	def post( self, URL, ARGS ):
		pass	

def main():
	bar = FRHTTPRequest('googleappengine')
	
	foo = bar.get('http://www.google.com')
	
	print foo
	print foo.header('connection')
	print foo.body()


if __name__ == '__main__':
	main()

