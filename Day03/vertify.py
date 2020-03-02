'''
@Time : 2020/1/7 10:30
@Author : wangmengying
@File : vertify.py
'''
user = input('请输入用户名:')
password = input('请输入密码：')
if user == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')