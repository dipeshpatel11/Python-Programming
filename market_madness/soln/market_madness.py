# Good luck!
days=input()
stocks=list(map(int,input().split()))

in_val,differnce,low_val = 0,0,stocks[0]

for i in stocks:
	if i<low_val or i==low_val:
		low_val=i
		high_val = max(stocks[in_val:])
		if high_val - low_val > differnce:
			differnce = high_val - low_val
	in_val +=1

print(differnce)
