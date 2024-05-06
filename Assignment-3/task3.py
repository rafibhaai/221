path  = r"input3.txt"
file_1 = open(path,"r")
input = file_1.readlines()
n = int(input[0])
input = input[1].split()
for i in range(int(n)):
    input[i] = int(input[i])
file_1.close()

def count_pairs(arr):
    n = len(arr)
    if n <= 1:
        return 0
    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    count = count_pairs(left_arr) + count_pairs(right_arr)

    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            count += len(left_arr) - i
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = left_arr[i]
            i += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return count

output = count_pairs(input)
path_2 = r"output3.txt"
file_2 = open(path_2,"w")
file_2.writelines(str(output))
file_2.close()