class bmi(object):
	def __init__(self,weight,height):
		self.weight=weight
		self.height=height
	def BMI():
		s=self.height/self.height**2
		if s>=35:
			print('您的BMI为%s,过于肥胖'%s)
		elif s>30:
			print('您的BMI为%s,肥胖'%s)
		elif s>25:
			print('您的BMI为%s,健康'%s)
		elif s>18.5:
			print('您的BMI为%s,偏轻'%s)
		elif s<18.5:
			print('您的BMI为%s,过轻'%s)
			