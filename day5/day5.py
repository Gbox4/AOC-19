f=open("day5/input.txt","r")
intcode=f.readline().split(",")
for i in range(len(intcode)):
    intcode[i] = int(intcode[i])

opParams = {
    1:3,
    2:3,
    3:1,
    4:1
}

codes=True
nParams=0
nParamsLeft=0
params=[]
paramModes=[]

for i in intcode:
    if codes:
        op=int(str(i)[-1])
        codes = False
        
        nParams=opParams[str(i)[-1]]
        nParamsLeft=nParams
        if len(str(i)) != 1:
            for j in range(2+nParams-len(str(i))):
                paramModes.append[0]
            for j in i[:-2]:
                paramModes.append[j]
    else:
        if paramModes[nParams-nParamsLeft]



print()