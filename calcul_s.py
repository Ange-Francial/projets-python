import numpy as np

e=np.array([[19, 11, 1],
[16, 19, 1],
[15, 11, 1],
[14, 6, 1],
[7, 14, 1],
[16, 15, 1],
[3, 19, 1],
[7, 15, 1]])

w=np.array([[2],[1],[-46]])
f=np.dot(e,w)
print(f)

for i in range(8):
    if f[i]>0 :
        f[i]=0
    else:
        f[i]=1

print("Les sorties sont : \n",f)
