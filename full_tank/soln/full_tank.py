# Good luck on this morning problem!

a,b,c,d = tuple(map(int, input().split()))
ti_list = list(map(int, input().split()))

time = a 
maximum_fuel = b

for i in range (0, len(ti_list)):
	if i ==0:
		b-= ti_list[i]
	else:
		b-= ti_list[i]
		b+= ti_list[i-1]

	if b>=0 and b<(a - ti_list[i]):
		if (i<=len(ti_list) - 2 and b<(ti_list[i+1] - ti_list[i])) or i == len(ti_list) -1:
			time += d 
			b = maximum_fuel

print(time)