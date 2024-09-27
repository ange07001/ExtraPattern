

def SmallestInt(n):
    i = 0
    kVal = []
    while True:
        k = 2*i+1
        kVal.append(k)
        if sum(kVal) > n:
            return k
        i+=1

def largestInt(n):
    i = 0
    kVal = []
    while True:
        k=2*i
        kVal.append(k)
        if sum(kVal) <= n and sum(kVal) + 2*(i+1) > n:
            return k
        i+=1


while True:
    try:
        Input = int(input("Enter a positive integer: "))
        if Input > 0:
            break
        else:
            print("\033[91m"+"Not a positive integer"+"\033[0m")
    except ValueError:
        print("\033[91m"+"Not a positive integer"+"\033[0m") 
print("-"*30)
print(f"The smallest k is: \033[92m{SmallestInt(Input)}\033[0m")
print(f"The largest k is: \033[92m{largestInt(Input)}\033[0m")
