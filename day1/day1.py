f=open("day1/input.txt","r")
contents = f.readlines()

total = 0

for i in contents:
    fuel = int(float(i)/3)-2
    total += fuel

    while fuel>0:
        fuel = int(float(fuel)/3)-2

    

    

print(total)