f=open("day3/input.txt","r")
wires=[]

for i in f.readlines():
    wires.append(i.split(","))



class Line():
    def __init__(self, x1,x2,y1,y2,length,sign):
        self.x1 = min(x1,x2)
        self.y1 = min(y1,y2)
        self.x2 = max(x1,x2)
        self.y2 = max(y1,y2)
    

        #left-right or up-down
        self.lr= y1==y2
        self.ud= x1==x2

        self.length=length
        self.sign=sign

def doLinesCross(l1,l2):
    #check if lines are parallel
    if (l1.lr and l2.lr) or (l1.ud and l2.ud):
        return False
    
    
    if l1.lr:
        lr = l1
        ud = l2
    
    else:
        lr = l2
        ud = l1
    
    if ud.x1 in range(lr.x1,lr.x2) and lr.y1 in range(ud.y1,ud.y2):
        return [ud.x1,lr.y1]
    
    else:
        return False

#these are lists of Line()


lines=[]



for w in range(2):
    lastx=0
    lasty=0
    wire = []
    for i in wires[w]:
        val = int(i[1:])
        if i[0]=="R":
            wire.append(Line(lastx,val+lastx,lasty,lasty,val,"R"))
            lastx=(lastx+val)

        elif i[0]=="L":
            wire.append(Line(lastx,lastx-val,lasty,lasty,val,"L"))
            lastx=(lastx-val)

        elif i[0]=="U":
            wire.append(Line(lastx,lastx,lasty,lasty+val,val,"U"))
            lasty=(lasty+val)

        elif i[0]=="D":
            wire.append(Line(lastx,lastx,lasty,lasty-val,val,"D"))
            lasty=(lasty-val)

    lines.append(wire)

matches = []

for l in lines[0]:
    for o in lines[1]:
        if doLinesCross(l,o) != False:
            matches.append(doLinesCross(l,o))


lowest = 999999
for i in matches:
    if lowest > abs(i[0])+abs(i[1]) and abs(i[0])+abs(i[1]) != 0:
        lowest = abs(i[0])+abs(i[1])


print(lowest)

#Part 2
steps=[]

llength=0
for l in lines[0]:
    

    olength=0
    
    for o in lines[1]:
        
        
        result = doLinesCross(l,o)
        if result != False:
            cross = [l,o]
            total = llength+olength

            for i in cross:
                if i.sign=="R":
                    total += abs(result[0]-i.x1)
                elif i.sign =="L":
                    total += abs(result[0]-i.x2)
                elif i.sign == "U":
                    total += abs(result[1]-i.y1)
                elif i.sign == "D":
                    total += abs(result[1]-i.y2)
            
            steps.append(total)
            
        olength+=o.length

    llength+=l.length


loweststeps = 99999
for i in steps:
    if loweststeps > i and i != 0:
        loweststeps = i
        #lowest= abs(i[0])+abs(i[1])
print(loweststeps)