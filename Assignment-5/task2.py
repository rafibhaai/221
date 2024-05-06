
import collections
f = open('input2.txt', 'r')
f1 = open('output2.txt', 'w')
var = f.read().split('\n')
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
  f1.write('IMPOSSIBLE')
else:

  in_deg = [0] * (int(ver)+1)
  for li in g.values():
    for node in li:
      in_deg[node] += 1
  print(in_deg)

  visited = [0] * (int(ver)+1)
  li = []
  q = collections.deque([])

  def bfs(graph):
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

  for i in range(1,int(ver)+1):
    if in_deg[i] == 0:
      q.append(i)
      y = bfs(g)
  for i in y:
    f1.write(str(i) + ' ')