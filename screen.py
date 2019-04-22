#-*- coding:utf-8 -*-
class BMI(object):
	def __init__(self,weight=0,height=0):
		self._weight=weight
		self._height=height
	@property
	def weight(self):
		return self._weight
	@weight.setter
	def weight(self,value):
		if not isinstance(value,float) or value<0:
		    raise ValueError('请输入大于零的数字')
		self._weight=value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		if not isinstance(value,float) or value<0:
		    raise ValueError('请输入大于零的数字')
		self._height=value
	@property
	def bmi(self):
		return self._weight/(self._height**2)
if bmi(self)>0:
	print ('you are fat')
	
		
			
	
    