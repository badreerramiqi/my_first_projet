n=int(input("entrer le nombre d'éléves : "))
notes={}
somme=0
for i in range(0,n):
    notes[i]=int(input("entrer la note :"))
    somme = somme + notes[i]
moyenne = somme / n
print("les notes qui sont au dessus de la moyenne : ")
for i in range(1,n):
    if notes[i]>=moyenne:
     print(notes[i],end=" ")

