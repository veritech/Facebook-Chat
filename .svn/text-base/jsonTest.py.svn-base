#!/usr/bin/env python
# encoding: utf-8
"""
jsonTest.py

Created by Jonathan Dalrymple on 2008-06-18.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import demjson
import logging

def main():

	#regex to extract the text i desire
	#\"time\".*\"notifications\"
	foo =  """
for(;;);{"error":0,"errorSummary":"","errorDescription":"No error.","payload":{"time":1213878377000,"buddy_list":{"listChanged":true,"availableCount":12,"nowAvailableList":{"280300914":{"i":false},"506651931":{"i":false},"506688044":{"i":false},"506799855":{"i":false},"676911075":{"i":false},"705370472":{"i":false},"737500787":{"i":false},"501007176":{"i":true},"504468711":{"i":true},"511980284":{"i":true},"517172652":{"i":true},"706953397":{"i":true}},"wasAvailableIDs":[],"userInfos":{"280300914":{"name":"Jessica Neale","firstName":"Jessica","thumbSrc":"http:\/\/profile.ak.facebook.com\/v225\/1628\/30\/q280300914_7654.jpg","status":null,"statusTime":0,"statusTimeRel":""},"506651931":{"name":"Jai Morjaria","firstName":"Jai","thumbSrc":"http:\/\/profile.ak.facebook.com\/v222\/1041\/95\/q506651931_3834.jpg","status":"is like please shut Alex up her singing is shit.","statusTime":1213826379,"statusTimeRel":"14 hours ago"},"506688044":{"name":"Scott Lambton","firstName":"Scott","thumbSrc":"http:\/\/profile.ak.facebook.com\/v52\/749\/21\/q506688044_8491.jpg","status":null,"statusTime":0,"statusTimeRel":""},"506799855":{"name":"Jason O'Dell","firstName":"Jason","thumbSrc":"http:\/\/profile.ak.facebook.com\/v226\/1106\/32\/q506799855_8932.jpg","status":"thinks horse racings a mugs game.","statusTime":1213863474,"statusTimeRel":"4 hours ago"},"676911075":{"name":"Leslie Cosmic Afriyie","firstName":"Leslie","thumbSrc":"http:\/\/profile.ak.facebook.com\/v226\/1994\/59\/q676911075_1041.jpg","status":"has had a very productive day! Hold tite Brick & Lace and their management...","statusTime":1213878163,"statusTimeRel":"3 minutes ago"},"705370472":{"name":"Alex McCarthy","firstName":"Alex","thumbSrc":"http:\/\/profile.ak.facebook.com\/v223\/401\/51\/q705370472_4651.jpg","status":"Knows His Comets Soilders Are Destined For Glory Sunday.","statusTime":1213873894,"statusTimeRel":"about an hour ago"},"737500787":{"name":"Jody Hinshelwood","firstName":"Jody","thumbSrc":"http:\/\/profile.ak.facebook.com\/v228\/559\/124\/q737500787_7721.jpg","status":"is dying!!! :(.","statusTime":1213723234,"statusTimeRel":"on Tuesday"},"501007176":{"name":"Mark Payne","firstName":"Mark","thumbSrc":"http:\/\/profile.ak.facebook.com\/v227\/1073\/119\/q501007176_7716.jpg","status":null,"statusTime":0,"statusTimeRel":""},"504468711":{"name":"Laura Maggie Finch","firstName":"Laura","thumbSrc":"http:\/\/profile.ak.facebook.com\/v222\/929\/19\/q504468711_2627.jpg","status":"is gainin bean points!!! woop woop x.","statusTime":1213630780,"statusTimeRel":"on Monday"},"511980284":{"name":"Nyikayedu Madziya","firstName":"Nyikayedu","thumbSrc":"http:\/\/profile.ak.facebook.com\/v225\/1189\/23\/q511980284_5775.jpg","status":"is liking Sirenia.","statusTime":1213872181,"statusTimeRel":"2 hours ago"},"517172652":{"name":"Fuad Williamson","firstName":"Fuad","thumbSrc":"http:\/\/profile.ak.facebook.com\/v223\/1644\/76\/q517172652_7659.jpg","status":null,"statusTime":0,"statusTimeRel":""},"706953397":{"name":"Rupert Dann","firstName":"Rupert","thumbSrc":"http:\/\/profile.ak.facebook.com\/v228\/1248\/119\/q706953397_2598.jpg","status":"play on... PLAYER!","statusTime":1213815271,"statusTimeRel":"18 hours ago"},"570347316":{"name":"Jonathan Dalrymple","firstName":"Jonathan","thumbSrc":"http:\/\/profile.ak.facebook.com\/v227\/346\/15\/q570347316_451.jpg","status":"wants to watch adulthood, y'knahmean.","statusTime":1213748400,"statusTimeRel":"on Tuesday"}},"forcedRender":true,"flMode":false,"flData":{}}},"bootload":[{"name":"js\/common.js.pkg.php","type":"js","src":"http:\/\/static.ak.fbcdn.net\/rsrc.php\/pkg\/60\/105143\/js\/common.js.pkg.php"}]}	"""

	#strip the preceeding for loop
	foo = foo[9:len(foo)]
	bar = demjson.decode( foo )
	
	logging.basicConfig( filename = 'test.log' )
	logging.log(10,'Test %d',20)
	
	print '=' * 10
	
	#print bar['payload']['buddy_list']
	print 'Users online %d' % bar['payload']['buddy_list']['availableCount']
	for user in bar['payload']['buddy_list']['nowAvailableList']:
		print bar['payload']['buddy_list']['userInfos'][user]['name']

if __name__ == '__main__':
	main()

