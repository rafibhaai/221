
inp = open('input3.txt','r')
out = open('output3.txt','w')
n, m = map(int, inp.readline().strip().split(" "))

adjList = [[] for j in range(n+1)]
for j in range(m):
    indices=list(map(int,inp.readline().split()))
    i=indices[0]
    j=indices[1]
    adjList[i].append(j)
    adjList[j].append(i)
#print(adjList)

def DFS(adjL,s):
   stack=[]
   vis=[0]*len(adjList)
   stack.append(s)
   vis[s]=1
   while len(stack)!=0:
      node=stack.pop()
      print(node,end=' ')
      for val in adjL[node]:
         if vis[val]==0:
            DFSvisit(adjL,val,stack,vis)

def DFSvisit(adjL,new_s,stack,vis):
    vis[new_s]=1
    stack.append(new_s)
    node=stack.pop()
    print(node,end=' ')
    for val in adjL[node]:
        if vis[val]==0:
          DFSvisit(adjL,val,stack,vis)
dfsList = DFS(adjList, 1)
#print(dfsList)