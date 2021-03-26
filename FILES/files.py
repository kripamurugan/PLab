f=open('myfiles.txt','r')
f1=open('o.txt','w')
f2=open('e.txt','w')
for i in map(int,f.readline().split()):
    if i%2!=0:
        f1.write(str(i)+' ')
    else:
        f2.write(str(i)+' ')
