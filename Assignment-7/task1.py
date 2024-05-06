
path = "/content/drive/MyDrive/CSE 221 LAB/LAB7/input1_1.txt"
path_2 = "/content/drive/MyDrive/CSE 221 LAB/LAB7/output1_1.txt"
input_file=open(path,"r")
output_file=open(path_2,"w")
var = int(input_file.readline())

queue = []
for i in range(var):
    x=input_file.readline().strip().split(" ")
    queue.append(x)

sort_queue =sorted(queue, key=lambda x: int(x[1]))

output_array = []
i = sort_queue[0]
output_array.append(i)
a=output_array[0][1]
for i in range(1, len(queue)):
    if a<=sort_queue[i][0]:
        output_array.append(sort_queue[i])
        a=sort_queue[i][1]

print(len(output_array), file=output_file)
for i in range(len(output_array)):
    print(output_array[i][0],output_array[i][1], file=output_file)
output_file.close()