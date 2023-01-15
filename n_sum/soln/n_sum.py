#Good Luck! You've got this! :)

n,m = map(int,input().split())
	
actual_sum = 0
values = []
for x in range(n,0,-1):
	if m > actual_sum + x:
		actual_sum = actual_sum + x
		values.append(x)
	elif m == actual_sum + x:
		values.append(x)
		break
	elif m < actual_sum + x:
		continue

print (len(values))
print(*values[::-1])

