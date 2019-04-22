H=float(input('请输入您的身高（m）:'))
W=float(input('请输入您的体重（kg）:'))
BMI=float(W/H/H)
print('您的BMI为%.2f'%BMI)
if BMI<18.5:
    print('体重过轻')
elif 18.5<=BMI<25:
    print('体重正常')
elif 25<=BMI<28:
    print('体重过重')
elif 28<=BMI<32:
    print('体重过重肥胖')
else:
    print('严重肥胖')