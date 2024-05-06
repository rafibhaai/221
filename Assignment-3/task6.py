path  = r"input6.txt"
file_1 = open(path,"w")

text = "9\n10 11 10 6 7 9 8 15 2 \n4 \n5 \n3 \n2 \n7"
file_1.writelines(text)
file_1.close()

file_1 = open(path,"r")
ini_input = file_1.readlines()
n = int(ini_input[0])
arr = ini_input[1].split()
queries = []
for i in range(2,len(ini_input)):
    queries += ini_input[i].split()
file_1.close()
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(queries)):
    queries[i] = int(queries[i])
test = queries[0]
queries = queries[1:]

def find_kth_smallest(arr, l, r, k):
	if (k > 0 and k <= r - l + 1):
		idx = partition(arr, l, r)
		if (idx - l == k - 1):
			return arr[idx]
		if (idx - l > k - 1):
			return find_kth_smallest(arr, l, idx - 1, k)

		return find_kth_smallest(arr, idx + 1, r,k - idx + l - 1)

def partition(arr, l, r):
	pivot = arr[r]
	i = l
	for j in range(l, r):
		if (arr[j] <= pivot):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i

output = ""
for k in range(test):
    result = find_kth_smallest(arr, 0, n-1, queries[k])
    output += str(result) + "\n"

path_2 = r"output6.txt"
file_2 = open(path_2,"w")
file_2.writelines(output)
file_2.close()