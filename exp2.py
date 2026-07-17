import random
import time
import string

def naive(t,p):
    c=0; m=[]
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            c+=1
            if t[i+j]!=p[j]: break
        else: m.append(i)
    return m,c

def kmp(t,p):
    l=[0]*len(p); j=0
    for i in range(1,len(p)):
        while j and p[i]!=p[j]: j=l[j-1]
        if p[i]==p[j]: j+=1; l[i]=j
    i=j=0; c=0; m=[]
    while i<len(t):
        c+=1
        if t[i]==p[j]: i+=1; j+=1
        elif j: j=l[j-1]
        else: i+=1
        if j==len(p): m.append(i-j); j=l[j-1]
    return m,c

def rk(t,p,q=101):
    d=256; n,m=len(t),len(p)
    h=pow(d,m-1,q); ph=th=0; c=0; pos=[]
    for i in range(m):
        ph=(d*ph+ord(p[i]))%q
        th=(d*th+ord(t[i]))%q
    for i in range(n-m+1):
        if ph==th:
            for j in range(m):
                c+=1
                if t[i+j]!=p[j]: break
            else: pos.append(i)
        if i<n-m: th=(d*(th-ord(t[i])*h)+ord(t[i+m]))%q
    return pos,c

#T=text
#P=pattern

t,p="AABAACAADAABAABA","AABA"
print("Naive:",naive(t,p))
print("KMP  :",kmp(t,p))
print("RK   :",rk(t,p))

T=''.join(random.choices('ABCD',k=10000))
print("\nPattern\tNaive\tKMP\tRK")
for p in ["AB","ABCD","ABCDAB","ABCDABCD"]:
    print(p,*[f(T,p)[1] for f in (naive,kmp,rk)],sep="\t")