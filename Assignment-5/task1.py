
#TAsk1a
import collections
f1 = open('input1.txt', 'r')
f2 = open('output1.txt', 'w')

var = f1.readlines()
#print(var)
ver, lines = var[0].split()

g = {}
for i in range(1,int(ver)+1):
  g[i] = []

for j in range(1,len(var)):
  s = var[j].split(' ')
  n1 = int(s[0])
  n2 = int(s[1])
  if n1 in g.keys():
    g[n1].append(n2)

print(g)

vis = []
visited2 = [0] * (int(ver)+1)
#print(visited)
st = collections.deque([])
def dfs(visited2,graph,s):
  flag = False
  if visited2[s] == 0:
    visited2[s] = 1
    vis.append(s)
    for adj_node in graph[s]:
      dfs(visited2,graph,adj_node)

  if s not in st:
    st.append(s)
  elif s in vis:
    flag = True
  return flag

for i in range(1,int(ver)+1):
  if visited2[i] != 1:
    x = dfs(visited2,g,i)
    if x:
      break
if x == False:
  for i in range(int(ver)):
    f2.write(str(st.pop()) + ' ')
else:
  f2.write('IMPOSSIBLE')

#TASk1b
import collections
f3 = open('input1.txt', 'r')
f4 = open('output1_2.txt', 'w')
var = f3.read().split('\n')
#print(var)
ver, lines = var[0].split()

g = {}
for i in range(1,int(ver)+1):
  g[i] = []

for j in range(1,len(var)):
  s = var[j].split(' ')
  n1 = int(s[0])
  n2 = int(s[1])
  if n1 in g.keys():
    g[n1].append(n2)

#print(g)

def cycle_detect(graph,source):
  global flag
  queue = collections.deque([source])
  visited = []
  while queue:
    v = queue.popleft()
    visited.append(v)
    for i in graph[v]:
      if i not in visited:
        queue.append(i)
        flag = False
      elif i in visited:
        flag = True
        break

  return flag
for i in range(1,int(ver)+1):
  x = cycle_detect(g,i)
if x == True:
  f4.write('IMPOSSIBLE')
else:

  def bfs(graph):


      in_deg = [0] * (int(ver)+1)
      for li in g.values():
        for node in li:
          in_deg[node] += 1
      #print(in_deg)

      visited = [0] * (int(ver)+1)
      li = []
      q = collections.deque([])
      for i in range(1,int(ver)+1):
        if in_deg[i] == 0:
          q.append(i)

      while q:
        vertex = q.popleft()
        if not visited[vertex]:
          li.append(vertex)
          for i in graph[vertex]:
            in_deg[i] -= 1
            if in_deg[i] == 0:
                q.append(i)
          visited[vertex] = 1

      return li
  y = (bfs(g))
  for i in y:
    f4.write(str(i)+' ')