'''
@Time : 2020/1/6 19:17
@Author : wangmengying
@File : strings.py
'''

strs = 'hello,world!'
print('字符串长度：',len(strs))
print('单词首字母大写:',strs.title())
print('字符串大写:',strs.upper())
print('字符串是否是大写：',strs.isupper())
print('字符串是否以hello开头：',strs.startswith('hello'))
print('字符串是否以hello结尾：',strs.endswith('hello'))
str1 = '-wangmengying'
str2 = strs.title() + ' ' + str1.lower()
print(str2)
