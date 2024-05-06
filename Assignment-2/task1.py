#1a
with open('input1.txt', 'r') as txt:
  a =txt.readline().strip().split(' ')
  #print(a)
  size,target =a
  #print(target)
  var = txt.readline().strip().split(' ')
  #print(var)

  lst=[]
  size = int(size)
  for i in range(size):
    sum = 0
    for j in range(i+1,size):
      var[i] = int(var[i])
      var[j] = int(var[j])
      sum=sum+var[i]+var[j]
      if sum == int(target):

        lst.append(i+1)
        lst.append(j+1)

  if len(lst) == 0:
    lst.append('IMPOSSIBLE')
with open('output1.txt', 'w') as fl:
  for i in lst:
    if type(i) == int:
      fl.write(str(i+1)+' ')
    else:
      fl.write(i)

#1b
with open('input1.txt', 'r') as text:
  a =text.readline().strip().split(' ')

  length,total =a
  var = text.readline().strip().split(' ')

  length = int(length)
  total = int(total)
  left = 0
  right = len(var)-1
  l = []
  while left < right:
    var[left] = int(var[left])
    var[right] = int(var[right])
    if var[left] + var[right] == total:

      l.append(left)
      l.append(right)
      break
    elif var[left] + var[right]>target:
      right-=1
    elif var[left] + var[right]<target:
      left+=1
  if len(l) == 0:
    l.append('IMPOSSIBLE')
with open('output1.txt', 'w') as b:
  for i in l:
    if type(i) == int:
      b.write(str(i+1)+' ')
    else:
      b.write(i)
