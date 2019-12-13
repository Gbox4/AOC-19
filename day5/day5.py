f=open("day2/input.txt","r")
intcode=f.readline().split(",")
for i in range(len(intcode)):
    intcode[i] = int(intcode[i])

original = list(intcode)

def updateBlocks(intcode):
    updatedBlocks = []
    for i in range(len(intcode)):
        block = []


        if i%4 != 0:
            continue
        else:
            if intcode[i] == 99:
                updatedBlocks.append([99])
                break

            else:
                for j in range(4):
                    block.append(intcode[i+j])
                updatedBlocks.append(block)
    
    return updatedBlocks



def computeIntcode(intcode):
    blocks = updateBlocks(intcode)
    b = blocks[0]
    stepNumber = 0

    while b[0] != 99:
        try:
            op=b[0]
            num1=intcode[b[1]]
            num2=intcode[b[2]]
            store=b[3]

            if op == 1:
                intcode[store] = num1+num2
            if op == 2:
                intcode[store] = num1*num2

            blocks = updateBlocks(intcode)
            stepNumber-=-1
            b = blocks[stepNumber]
        except:
            break
    
    return (intcode)

intcode = computeIntcode(intcode)
