n=int(input("entrer un nombre : "))
c=0
for i in range(1,n+1):
  if n%i==0:
    print(i,"est un diviseur de ce nombre est :",n)
    c=c+1
print("Le nombre de diviseur est :",c)