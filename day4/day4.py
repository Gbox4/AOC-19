#input is 168630-718098
inputMin = 168630
inputMax = 718098

"""total = 0
for i in range(inputMin,inputMax):

    if len(str(i)) == 6:

        double = False
        decrease = False

        for c in range(5):
            if str(i)[c] == str(i)[c+1]:
                double = True
            if int(str(i)[c]) > int(str(i)[c+1]):
                decrease = True
                
        if double and not decrease:
            total += 1

print(total)"""

# Part 2

total = 0
for i in range(inputMin,inputMax):




    if len(str(i)) == 6:

        double = False
        decrease = False


        cchain=1
        lastc=None
        for c in range(6):
            currentc = str(i)[c]
            if currentc==lastc:
                cchain-=-1
            
            #when chain is broken
            if currentc!=lastc or c ==5:
                if cchain == 2:
                    double = True
                cchain = 1
            lastc=currentc


            try:
                if int(str(i)[c]) > int(str(i)[c+1]):
                    decrease = True
            except:
                pass
                
        if double and not decrease:
            total-=-1

print(total)