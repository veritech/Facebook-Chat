#!/usr/bin/env python
# encoding: utf-8
"""
dict.py

Created by Jonathan Dalrymple on 2008-06-22.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import UserDict
import pickle
import types
import copy

class SerializableDictionary( UserDict.IterableUserDict ):
	
	def __init__(self, uid = None):
		UserDict.UserDict.__init__(self)
		self.uid = uid


	def setUID(self, UID):
		pass
		
	def serialize(self):
		
		#use the uid to store the data
		return pickle.dumps( self.data )
		
	def serializeToFile(self, fh ):
		pickle.dump( self.data, fh )
	
	#Doest the heavy lifting for the deserialization
	def __loadSerializedDict(self, obj):
		if type(obj) == types.DictType:
			self.data = None
			self.data = obj.copy()
		else:
			raise 'Serialized %s is not a Dict Type, load failed' % type(obj)
			
	def load(self, str ):
		self.__loadSerializedDict( pickle.loads( str ) )
		
	def loadFromFile(self, fh ):		
		self.__loadSerializedDict( pickle.load( fh ) )

def main():
	
	bar = SerializableDictionary()
	
	bar['one'] = 'Jonathan'
	bar['two'] = 'Dalrymple'
	
	fh = open('temp.dat','w')
	foo = bar.serializeToFile( fh )
	
	x = SerializableDictionary( fh )
	
	fh.close()
	
	ah = open('temp.dat','r')
	
	x.loadFromFile( ah )
	
	for i in x:
		print x[i]
	

if __name__ == '__main__':
	main()

