import math # you may use math.sqrt(x), but you do not have to.

import math

n = int(input())

x, y, r = [], [], []
# x, y, r are empty lists

for i in range(n):
    x_in, y_in, r_in = map(float, input().split())
    x.append(x_in)
    y.append(y_in)
    r.append(r_in)

o = int(input())

x1, y1 = [], []
# x, y, r are empty lists

for i in range(o):
    x1_in, y1_in = map(float, input().split())
    x1.append(x1_in)
    y1.append(y1_in)

for i in range(o):
	xtest = x1[i]
	ytest = y1[i]
	q = 'Small'

	for j in range(n):
		if math.sqrt(abs(x[j]-xtest)**2 + abs(y[j]-ytest)**2) <= r[j]:
			q = 'Large'
			
	print(q)