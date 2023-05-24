a=int(input('Введите число '))
a1=a%1000
a2=a//1000
sum1=a1//100+a1//10%10+a1%10
sum2=a2//100+a2//10%10+a2%10
if sum1==sum2:
    print(a,'-','yes')
else:    
    print(a,'-','no')