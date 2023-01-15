# add your solution here

n = int(input())
levels = {}
for i in range(n):
	m = int(input())
	try:
		levels[m] +=1
	except:
		levels[m] = 1

ctn = 0
for i in range(max(levels)):
	try:
		ctn += levels[i]
		print(n-ctn)
	except KeyError:
		print(n-ctn)
		continue
		