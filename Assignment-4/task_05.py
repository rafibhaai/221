

inp = open('input5.txt','r')
out = open('output.txt','w')
n, m, d = map(int, inp.readline().strip().split(" "))

adjList = [[] for j in range(n+1)]
for j in range(m):
    indices=list(map(int,inp.readline().split()))
    i=indices[0]
    j=indices[1]
    adjList[i].append(j)
    adjList[j].append(i)

def BFS(adjL, s):
    queue = []
    dis= [10**8]*len(adjL)
    sp=['']*len(adjL)
    queue.append(s)
    dis[s] = 0
    sp[s]=str(s)
    while len(queue)!=0:
       node = queue.pop(0)
       for val in adjL[node]:
           if dis[node]+1 < dis[val]:
               dis[val]=dis[node]+1
               sp[val]+=sp[node]+f' {str(val)}'
               queue.append(val)
    return dis,sp

bfsList = BFS(adjList, 1)
time,short_path=bfsList
out.write(f'Time:{time[d]}\nshortest path:{short_path[d]}')