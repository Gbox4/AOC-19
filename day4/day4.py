#input is 168630-718098
inputMin = 168630
inputMax = 718098

total = 0
for i in range(inputMin,inputMax):
    if len(str(i)) < 6:
        continue

    double = False
    decrease = False
    
    for c in range(len(str(i))):
        if c > 0 and c < len(str(i))-1:
            if str(i)[c] == str(i)[c+1]:
                double = True
            if int(str(i)[c]) < int(str(i)[c+1]):
                decrease = True
            
    if double and not decrease:
        total += 1

print(total)