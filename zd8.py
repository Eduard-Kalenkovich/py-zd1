n=int(input('Введите число n '))
m=int(input('Введите число m '))
k=int(input('Введите число k '))
if (n*m-k)%2==0:
    print(n,' ', m,' ', k,'-yes ')
else:
    print(n,' ', m,' ', k,'-no ')