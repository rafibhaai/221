path  = r"input1.txt"
file_1 = open(path,"w")
text = "8\n9 5 4 6 1 3 2 9"
file_1.writelines(text)
file_1.close()

file_1 = open(path,"r")
input = file_1.readlines()
n = int(input[0])
input = input[1].split()
for i in range(int(n)):
    input[i] = int(input[i])
file_1.close()


def merge(a, b):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = mergeSort(arr[:mid])
        right_half = mergeSort(arr[mid:])
        return merge(left_half, right_half)


sorted_list = mergeSort(input)
print("Sorted list:", sorted_list)
output =""
for i in sorted_list:
    output += str(i) + " "

path_2 = r"output1.txt"
file_2 = open(path_2,"w")
file_2.writelines(str(output))
file_2.close()