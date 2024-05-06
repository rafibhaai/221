
inp = open('input4.txt','r')
out = open('output4.txt','w')
V, e = map(int, inp.readline().strip().split(" "))

adjList = [[] for j in range(V+1)]
for j in range(e):
    indices=list(map(int,inp.readline().split()))
    i=indices[0]
    j=indices[1]
    adjList[i].append(j)
#print(adjList)

def DFS(adjL,s,V):
   color=["white"]*(V+1)
   global cycle
   cycle='No'

   for u in range(1,(V+1)):
     if color[u]=='white':
       #time+=1
       DFSvisit(adjL,u,color)
def DFSvisit(adjL,curr,color):
    color[curr]='grey'
    for v in adjL[curr]:
        if color[v]=='white':
          DFSvisit(adjL,v,color)
        elif color[v]=='grey':
          global cycle
          cycle='yes'
    color[curr]='black'

dfsList = DFS(adjList, 1,V)
out.write(cycle)