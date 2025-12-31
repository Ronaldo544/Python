num = 1094573458274924624527423598043756309852375936012513264583

flag = False
if num > 1: 
    #check for factors
    for i in range(2,num):
        if (num % i) ==0:
            flag = True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")