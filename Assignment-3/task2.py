path  = r"input2.txt"
file_1 = open(path,"w")
text = "8\n1 7 13 4 5 7 13 12"
file_1.writelines(text)
file_1.close()

file_1 = open(path,"r")
input = file_1.readlines()
n = int(input[0])
input = input[1].split()
for i in range(int(n)):
    input[i] = int(input[i])
file_1.close()
def find_maximum(arr):

    if len(arr) == 1:
        return arr[0]

    else:
        mid = len(arr) // 2
        left_max = find_maximum(arr[:mid])
        right_max = find_maximum(arr[mid:])
        return max(left_max, right_max)

output = find_maximum(input)
path_2 = r"output2.txt"
file_2 = open(path_2,"w")
file_2.writelines(str(output))
file_2.close()