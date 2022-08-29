
num=int(input("enter random number: "))

flag=False

if num<=1:
    print(num,' is NOT a prime number')
else:
    for i in range(2,num-1):
        if num%i == 0:
            flag=True
            break
if flag:
    print(num, ' is NOT a prime number')
else:
    print(num, ' is  a prime number')
