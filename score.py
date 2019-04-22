#-*- coding:utf-8 -*-
class student(object):
	__slots__=('score')
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		
		if not isinstance(value,int):
			raise ValueError('geshicuowu')
		if value<0 or value>100:
			raise ValueError('score must be in 0~100')
		else:
			self._score=value