a={1:2,3:4,4:3,2:1,0:0}
b={}
c=list(a.items())
print(c)
v=a.values()
for i in range(len(c)):
    for j in range(0,len(c)-i-1):
        if c[j][1]>c[j+1][1]:
            print(c[j+1][1])
            c[j],c[j+1]=c[j+1],c[j]
for k,v in c:
    b[k]=v
print(b)







