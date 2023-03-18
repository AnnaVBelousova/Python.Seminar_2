
S = int(input())
P = int(input())
for i in range(1, 11):
    for a in range (1, 11):
        if i+a == S and i*a ==P:
            num1 = i
            num2 = a

       
print(num1)
print(num2)