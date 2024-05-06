

path = "/content/drive/MyDrive/CSE 221 LAB/LAB7/input2_1.txt"
path_2 = "/content/drive/MyDrive/CSE 221 LAB/LAB7/output2_1.txt"
input_file=open(path,"r")
output_file=open(path_2,"w")
var=input_file.readline().split(" ")
number_of_task=int(var[0])
number_of_people=int(var[1])

task=[]
for i in range(number_of_task):
    var=input_file.readline().split(" ")
    start=int(var[0])
    end=int(var[1])
    task.append((start, end))

task.sort(key=lambda x: x[1])
end=[0]*number_of_people
counter=0

for k in task:
    start_time,end_time=k
    for i in range(number_of_people):
        if end[i]<=start_time:
            end[i]=end_time
            counter += 1
            break

print(counter,file=output_file)
output_file.close()