
#Task-02
inp = open('input2.txt','r')
out = open('output2.txt','w')
n, m = map(int, inp.readline().strip().split(" "))

adjList = [[] for j in range(n+1)]
for j in range(m):
    indices=list(map(int,inp.readline().split()))
    i=indices[0]
    j=indices[1]
    adjList[i].append(j)
    adjList[j].append(i)
#print(adjList)
def BFS(adjL, s):
    queue = []
    visited = [0]*len(adjL)
    result=''
    queue.append(s)
    visited[s] = 1
    while len(queue)!=0:
       node=queue.pop(0)
       result+=str(node)+' '
       for i in range(len(adjL[node])):
           if visited[adjL[node][i]] == 0:
               visited[adjL[node][i]] = 1
               queue.append(adjL[node][i])
    return result
bfs= BFS(adjList, 1)
print(bfs,file=out)