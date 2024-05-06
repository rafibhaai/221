
#Task_01(a)
inp=open('input1.txt','r')
out=open('output1.txt','w')
u,v=tuple(map(int,inp.readline().split()))
#print(u,v)
matrix = [[0]*(u+1) for i in range(0, u+1)]
#print(matrix)
for i in range(v):
   u,v,w=tuple(map(int,inp.readline().split()))
   matrix[u][v]=w
print(matrix,file=out)

#Task-01(b)

inp=open('inputb.txt','r')
out=open('outputb.txt','w')
u,v=tuple(map(int,inp.readline().split()))
#print(u,v)
matrix = [[] for i in range(0, v+1)]
print(matrix)
for i in range(v):
   u,v,w=tuple(map(int,inp.readline().split()))
   matrix[u].append((v,w))
#print(matrix)
for i in range(u+1):
   print(i,':',str(matrix[i]).strip('[]'),file=out)
out.close()