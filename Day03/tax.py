'''
@Time : 2020/1/7 11:23
@Author : wangmengying
@File : tax.py
'''

salary = float(input('年度总收入：'))
insurance = float(input('三险一金+专项：'))
diff = salary - insurance - 60000
if diff <= 0:
    rate = 0
    tax = 0
elif diff <= 36000:
    rate = 0.03
    tax = diff  * rate
elif diff <= 144000:
    rate = 0.1
    tax = 1080 + (diff - 36000) * rate - 2520
elif diff <= 300000:
    rate = 0.2
    tax = 1080 + 10800 + (diff - 144000) * rate - 16920
elif diff <= 420000:
    rate = 0.25
    tax = 1080 + 10800 + 31200 + (diff - 300000) * rate - 31920
elif diff <= 660000:
    rate = 0.3
    tax = 1080 + 10800 + 31200 + 30000 + (diff - 420000) * rate - 52920
elif diff <= 960000:
    rate = 0.35
    tax = 1080 + 10800 + 31200 + 30000 + 72000 + (diff - 660000) * rate - 85920
else:
    rate = 0.45
    tax = 1080 + 10800 + 31200 + 30000 + 72000 + 135000 + (diff - 960000) * rate - 181920
print(tax)
