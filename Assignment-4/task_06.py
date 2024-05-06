
def flood(arr, x, y, X, Y):
    if 0 <= x < X and 0 <= y < Y and arr[y][x] in "D.":
        val = 0
        if arr[y][x] == "D":
            val += 1
        arr[y] = arr[y][:x] + " " + arr[y][x + 1:]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                val += flood(arr, x + i, y + j, X, Y)
        return val
    else:
        return 0

with open('input6.txt', 'r') as file:
    lines = file.readlines()
    y, x = map(int, lines[0].split())
    arr = lines[1:]

max_d = 0

for j in range(y):
    for i in range(x):
        val = flood(arr, i, j, x, y)
        max_d = max(max_d, val)

with open('output6.txt', 'w') as file:
    file.write(f"{max_d}\n")
    file.write(arr[0])