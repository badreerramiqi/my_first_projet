n =int(input("entrer un entier n :"))
print("Les nombres entiers premiers inférieurs à ",n," sont :")
for i in range(1,n):
    premier=1
    j=2
    while j<i :
        if i%j==0:
            premier=0
        j=j+1
    if premier==1:
        print(i,end=" ")
