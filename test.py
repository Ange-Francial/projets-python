from random import random
import math
import numpy as np
from pylab import*

delta=0.1

k=0        #compteur de condition d'arrêt

#Entrer des différentes valeurs de e0, e1 et e2
x=np.array([[1,1,2/3,1/3],
            [1,1/3,1/3,1/3],
            [1,1/3,2/3,1]])

#Entrer des sorties désirées
y=np.array([0,1,1])

#Initialisation alléatoire des coéfficients synaptiques(Poids) des entrées
w0=random()
w1=random()
w2=random()
w3=random()

# w0=0
# w1=1
# w2=-1
w=np.array([[w0],[w1],[w2],[w3]])
print("Les coéfficients synaptiques(Poids) respectivement des entrées e0, e1 et e2 sont : ",w)
f=np.dot(x,w) #calcul de f pour chaque enregistrement

print (f) #affichage

#affectation des valeurs en sorties du perceptron dans f
for i in range(5):
    if f[i]>0 :
        f[i]=1
    else:
        f[i]=0
print(f)    #affichage des valeurs en sorties du perceptron dans f

#RECHERCHE DES POIDS
while k<250:
    for i in range(4):
        #calcul des nouveaux poids
        w0=w0+delta*(y[i]-f[i])*x[i,0]
        w1=w1+delta*(y[i]-f[i])*x[i,1]
        w2=w2+delta*(y[i]-f[i])*x[i,2]
        k=k+1


        w=([w1,w2,w0])
        f=np.dot(x,w)   #Calcul de la nouvelle valeur de f
        #affectation des nouvelles valeurs en sorties du perceptron dans f
        for i in range(4):
            if f[i]>0 :
                f[i]=1
            else:
                f[i]=0
print (f)
print (w)
