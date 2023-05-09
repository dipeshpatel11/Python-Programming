ISBN = '3-598-21508-8'
num_string = ISBN.replace('-','',3)

total = 0

for i,j in zip(iter(str(num_string)),range(10,0,-1)):
    multiply = (int(i)*j)
    total = total + multiply
    
validate = total%11

print(validate == 0)
