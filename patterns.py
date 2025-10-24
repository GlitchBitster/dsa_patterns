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

print("----Pattern A----")
PatternA(5)

print("----Pattern B----")
PatternB(5)

print("----Pattern C----")
PatternC(5)

print("----Pattern D----")
PatternD(5)

print("----Pattern E----")