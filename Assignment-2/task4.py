inp = open('input4.txt',"r")
x = inp.readline()
x = x.split(" ")
N = int(x[0])
M = int(x[1])
output = open('output4.txt',"w")

def maximize_tasks(tasks, num_people):
    tasks.sort(key=lambda x: x[1])
    completed_tasks = 0
    end_times = [0] * num_people

    for task in tasks:
        start, end = task
        for i in range(num_people):
            if start >= end_times[i]:
                end_times[i] = end
                completed_tasks += 1
                break

    return completed_tasks


tasks = []
for _ in range(N):
    start, end = map(int, inp.readline().split())
    tasks.append((start, end))


completed_tasks = maximize_tasks(tasks, M)


print(completed_tasks, file = output)
output.close()