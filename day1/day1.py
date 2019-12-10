f=open("day1/input.txt","r")
contents = f.readlines()

total = 0

for i in contents:
    fuel = int(float(i)/3)-2

    while fuel>0:
        total += fuel
        fuel = int(float(fuel)/3)-2

    

    

print(total)