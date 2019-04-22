def bmi():
    h=float(input('请输入身高'))
    w=float(input('请输入体重'))
    s=w/h/h
    print('您的BMI为%.2f'%s)
    if s<18.5:
        print('体重过轻')
    elif 18.5<=s<25:
        print('体重正常')
    elif 25<=s<28:
        print('体重过重')
    elif 28<=s<32:
        print('体重过重肥胖')
    else:
        print('严重肥胖')

bmi()