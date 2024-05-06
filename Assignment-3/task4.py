path  = r"input4.txt"
file_1 = open(path,"w")

text = "8\n5 10 4 -3 1 6 -10 2"
file_1.writelines(text)
file_1.close()

file_1 = open(path,"r")
input = file_1.readlines()
n = int(input[0])
input = input[1].split()
for i in range(int(n)):
    input[i] = int(input[i])
file_1.close()

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = 0
    j = 0
    k = l
    max_val = float('-inf')

    while i < n1 and j < n2:
        if L[i] + R[j] ** 2 > max_val:
            max_val = L[i] + R[j] ** 2
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return max_val


def max_mergeSort(arr, l, r):
    max_val = float('-inf')

    if l < r:
        m = (l + r) // 2
        max_val = max(max_val, max_mergeSort(arr, l, m))
        max_val = max(max_val, max_mergeSort(arr, m + 1, r))
        max_val = max(max_val, merge(arr, l, m, r))

    return max_val


def findMaxValue(arr):
    if len(arr) < 2:
        return float('-inf')
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    return max_mergeSort(arr, 0, len(arr) - 1)



max_val = findMaxValue(input)
path_2 = r"output4.txt"
file_2 = open(path_2,"w")
output = str(max_val)
file_2.writelines(output)
file_2.close()