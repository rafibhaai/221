import collections
f = open('input3.txt', 'r')
f2 = open('output3.txt', 'w')
var = f.read().split('\n')
ver, edges = var[0].split()

g = {}
for i in range(1,int(ver)+1):
  g[i] = []

for j in range(1,len(var)):
  n1, n2 = var[j].split()
  n1 = int(n1)
  n2 = int(n2)
  if n1 in g.keys():
    g[n1].append(n2)

#print(g)

visited = []

st = collections.deque([])
def dfs1(visited,graph,root):
  if root not in visited:
    visited.append(root) # 1 2 3
    for i in graph[root]:
      if i not in visited:
        dfs1(visited,graph,i)
    st.append(root)

  return st

dfs1(visited,g,1)
for i in range(1,int(ver)+1):
  if i not in visited:
    visited.append(i)
    st.append(i)
n_g = {}
for i in range(1,int(ver)+1):
  n_g[i] = []
for j in range(1,len(var)):
  n1, n2 = var[j].split()
  n1 = int(n1)
  n2 = int(n2)
  if n2 in n_g.keys():
    n_g[n2].append(n1)
#print(n_g)
v = []
li = []
lst = []
def print_scc(li,v,g,s):
    if s not in v:
      v.append(s)
      li.append(s)
      for i in g[s]:
          print_scc(li,v,g,i)
    return li
for i in range(int(ver)):
    s = st.pop()
    x = print_scc(li,v,n_g,s)
    li = []
    lst.append(x)
#print(lst)
scc_lst = sorted(lst)
for i in scc_lst:
  i.sort()
#print(scc_lst)
for i in scc_lst:
  if len(i) != 0:
    f2.write(' '.join(map(str,i)))
    f2.write('\n')