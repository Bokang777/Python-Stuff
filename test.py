num1 = input()
num2 = input()
Fibonacci_list =[]

def Fibonacci(num1,num2):
    i=1
    Fibonacci_list.append(num1)
    while i < 10:
        nextFib = num1 + num2
        num1 = num2
        num2 = nextFib
        Fibonacci_list.append(num1)
        i+=1
    return str(Fibonacci_list)
Fibonacci(num1, num2)
print("Fibonacci sequence:")
for x in range(len(Fibonacci_list)):
        print (Fibonacci_list[x], end =" ")






Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
num3 = int(input())

def Fibonacci(num1,num2,num3):
    i=1
    Fibonacci_list.append(num1)
    while i < num3:
        nextFib = num1 + num2
        num1 = num2
        num2 = nextFib
        Fibonacci_list.append(num1)
        i+=1
    print(Fibonacci_list)
    
Fibonacci(num1, num2, num3)






Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
i = 1
inp = int(input())
Fibonacci_list.append(num1)
while i < inp:
    nextFib = num1 + num2
    num1 = num2
    num2 = nextFib
    Fibonacci_list.append(num1)
    i+=1
print(Fibonacci_list)






num1 = int(input())
num2 = int(input())
next = num1 + num2
print(next)