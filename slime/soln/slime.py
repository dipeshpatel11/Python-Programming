# Good luck! This is your final python morning problem!
n = int(input())
outcome = []
outcome.append(1)
count = 1
while count <= (n-1):

    outcome.append(1)

    while (len(outcome) > 1) and (outcome[len(outcome) -1] == outcome[len(outcome) -2]):
        outcome.pop(len(outcome)-1)
        outcome[len(outcome)-1] = outcome[len(outcome)-1] + 1

    count += 1

print (*outcome)
        
    
    
