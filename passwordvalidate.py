def validate(password):



    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digit = [1,2,3,4,5,6,7,8,9,0]
    special = ['!','-','$','%','&','(',')','*','+',',','.','/',':',';','<','=','>','?','_','[',']','^','`','{','|','}','~']
    forbid = [' ','@','#']

    a = len(password)
    b = 1    # pass len b=1 true b=0 false
    c = 0    # special f=0 false f=1 true
    d = 1    # forbid e=0 false e=1 true
    e = 0    # upper e=0 false e=1 true
    f = 0    # lower f=0 false f=1 true 
    g = 0    # digit f=0 false f=1 true
   
    if a < 8:
      b = 0
    else:
     b=1


    for x in range(0,a):
        for y in range(0,3):
            if password[x] == forbid[y]:
                d=0

    for x in range(0,a):
        for y in range(0,26):
            if password[x] == upper[y]:
                e=1

    for x in range(0,a):
    	for y in range(0,26):
    		if password[x]  == lower[y]:
    		   f=1
    
    for x in range(0,a):    
    	for y in range(0,26):
            if password[x] == special[y]:
                c=1

    for x in range(0,a):
	    for y in range(0,10):
    		if password[x]  == digit[y]:
    		    g=1

    if b ==0 or d==0:
    	return "invalid"
    
    elif e ==0 or f==0 or c==0:
    	return "Insecure"
    
    else:
    	return "Secure"


import string
import random

def generate(n):

	letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
	result_str = "".join(random.choice(letters) for i in range(n))
	print(result_str)

generate(8)


if __name__ == '__main__':
    print(validate('Week1A$sgnment'))