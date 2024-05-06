

path = "/content/drive/MyDrive/CSE 221 LAB/LAB7/input3_1.txt"
path_2 = "/content/drive/MyDrive/CSE 221 LAB/LAB7/output3_1.txt"
input_file=open(path,"r")
output_file=open(path_2,"w")
var=input_file.readline().split(" ")
number_of_people=int(var[0])
queries=int(var[1])

parent_node=[0]*(number_of_people+1)
for i in range(len(parent_node)):
    parent_node[i]=i

size=[0]*(number_of_people+1)
for i in range(1,len(size)):
    size[i]=1

def find_parent(node,parent_node):
    if node==parent_node[node]:
        return node
    else:
        parent_node[node]=find_parent(parent_node[node],parent_node)
        return parent_node[node]

def union(a,b,parent_node,size):
    x=find_parent(a,parent_node)
    y=find_parent(b,parent_node)
    if x!=y:
        parent_node[y]=parent_node[x]
        size[x]=size[x]+size[y]
    return size[x]

for j in range(queries):
    value=var=input_file.readline().strip().split(" ")
    a=int(value[0])
    b=int(value[1])
    call_union=union(a,b,parent_node,size)
    print(call_union,file=output_file)
output_file.close()