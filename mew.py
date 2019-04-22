class bmi(object):
	def __init__(self,weight,height):
		self.weight=weight
		self.height=height
	def tizhong(self):
		self.s=self.weight/self.height/self.height
		if self.s>=35:
			print('您的BMI为%s,过于肥胖'%self.s)
		elif self.s>30:
			print('您的BMI为%s,肥胖'%self.s)
		elif self.s>25:
			print('您的BMI为%s,健康'%self.s)
		elif self.s>18.5:
			print('您的BMI为%s,偏轻'%self.s)
		elif self.s<18.5:
			print('您的BMI为%s,过轻'%self.s)
			
miao=bmi(57,1.54)
print(miao.tizhong())
