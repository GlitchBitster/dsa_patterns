def PatternA(num):
    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print("")

def PatternB(num):
    for i in range(num):
        for j in range(num):
            print(i + 1, end=" ")
        print("")

def PatternC(num):
    for i in range(num):
        for j in range(i+1):
            print("*", end=" ")
        print("")
        
def PatternD(num):
    for i in range(num):
        for j in range(i+1):
            print(j+ 1, end=" ")
        print("")

def PatternE(num):
    value = 0
    for i in range(num):
        value = 0 if (i+1) % 2 == 0 else 1
        for j in range(i + 1):
            print(value, end=" ")
            value = int(not value)
        print("") 

def PatternF(num):
    value = 1
    for i in range(num):
        for j in range(i + 1):
            print(value, end=" ")
            value += 1
        print("") 

def PatternG(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print(" ")       

def PatternH(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print(" ")     

def PatternI(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print(j+1, end=" ")
        print(" ")           



print("----Pattern A----")
PatternA(5)

print("----Pattern B----")
PatternB(5)

print("----Pattern C----")
PatternC(5)

print("----Pattern D----")
PatternD(5)

print("----Pattern E----")
PatternE(5)

print("----Pattern F----")
PatternF(5)

print("----Pattern G----")
PatternG(5)

print("----Pattern H----")
PatternH(5)

print("----Pattern I----")
PatternI(5)