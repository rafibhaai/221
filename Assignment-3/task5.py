path  = r"input5.txt"
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

def partition(array, low, high):

	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

data = input
size = len(data)
quickSort(data, 0, size - 1)

path_2 = r"output5.txt"
file_2 = open(path_2,"w")
final_output = ""
for i in data:
    final_output += str(i) + " "
file_2.writelines(str(final_output))
file_2.close()