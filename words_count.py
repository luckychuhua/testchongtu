# -*-coding:utf-8 -*-
num=0
dt={}
book=open('/Users/ll/Desktop/abcdef.txt')
for i in book:
	works=i.lower().split()
	for j in works:
		try:
			num=dt[j]
			dt[j]=num+1
		except Exception as e:
			dt[j]=1


print dt

		
#测试git	
