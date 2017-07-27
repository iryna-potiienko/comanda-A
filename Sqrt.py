import random
def sqrt(a,b):
    S = a * b
    print(S)
    return S
N=int(input('Enter your N:'))
for i in range(N):
    a=random.randint(1,100)
    b=random.randint(1,100)
    sqrt(a,b)
    C=10000
    S=1
    if S<C:
        C=S

print('S=',C)