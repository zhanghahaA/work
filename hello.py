#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Test(object):
	'''
	用于初始化类
	'''
	def __init__(self,a,b):
		self.a=a
		self.b=b
		
	def res(self):
		return (self.a,self.b)
	
t=Test(100,200)
print(t.res())