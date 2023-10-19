N=int(input("entrer la taille des tableu T1 et T2 : "))
T1={}
T2={}
S={}
print("Pour le tableau T1 :")
for i in range(0,N):
    T1[i]=int(input("entrer la valeur prochaine:"))
print("Pour le tableau T2 :")
for i in range(0,N):
    T2[i]=int(input("entrer la valeur prochaine:"))
print("Le tableau en somme :")
for i in range(0,N):
    S[i]=T1[i]+T2[i]
    print("Somme[",i,"] = ",S[i])