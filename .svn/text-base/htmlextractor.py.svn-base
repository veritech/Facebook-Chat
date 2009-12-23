#!/usr/bin/env python
# encoding: utf-8
"""
HTMLExtractor.py

Created by Jonathan Dalrymple on 2008-06-23.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sgmllib

class HTMLExtractor( sgmllib.SGMLParser ):
	def __init__(self, verbose = 0):
		sgmllib.SGMLParser.__init__(self, verbose)
		
		self.inError = False
		self.inLink = False
		self.linkStr = None
		self.postFormId = None
		
	
	def parse( self, str ):
		self.feed( str )
		self.close()
	
	
	#the tag we are looking for looks like ...
	#<a href="http://www.facebook.com/profile.php?id=570347316" class="profile_nav_link">Profile</a>
	
	def start_a( self, attr ):
		for name, value in attr:
			#becuase href occurs before the identity is confirmed save each href
			#This logic can be replaced with a reg ex, please do, this is kinda low, even for you
			if name == 'href':
				self.linkTemp = value
			
			if name == 'class' and value == 'profile_nav_link':
				self.inLink = True
				self.linkStr = self.linkTemp
				#print self.linkStr
				break
				
	def end_a( self ):
		self.inLink = False

	#Looking for post form id
	#<input type="hidden" id="post_form_id" name="post_form_id" value="" />
	def start_input(self, attr ):
		for name,value in attr:
			if name == 'id' and value == 'post_form_id':
				#print attr
				self.postFormId = attr[3][1]
				break
		
	def end_input( self ):
		pass

	def start_div( self, attr ):
		for name, value in attr:
			if name == 'id' and value =='error':
				self.inError = True
		
	def handle_data( self, str):
		if self.inError :
			print str
		
		
	def end_div( self ):
		self.inError = False

