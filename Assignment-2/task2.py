with open('input2.txt','r') as f:
  var = f.readlines()
  size = int(var[0])
  l1 = var[1].strip().split(' ')
  l2 = var[3].split(' ')
  arr = l1+l2
  #print(arr)
  def merge(a,b):
    i = 0
    j = 0
    lst = []
    length = len(a)+len(b)
    for k in range(length):
      # a[i] = int(a[i])
      # b[j] = int(b[j])
      if i < len(a) and j < len(b):
        if int(a[i]) < int(b[j]):
          lst.append(a[i])
          i+=1
        else:
          lst.append(b[j])
          j+=1
      else:
        if i < len(a):
          lst.append(a[i])
          i+=1
        elif j < len(b):
          lst.append(b[j])
          j+=1
    return lst
  def mergeSort(arr):
    #print(arr)
    if len(arr) <= 1:
      return arr
    else:
      mid = len(arr)//2
      a1 = mergeSort(arr[:mid]) # write the parameter
      a2 = mergeSort(arr[mid:]) # write the parameter
      return merge(a1, a2)

  l = mergeSort(arr)
  print(l)
with open('output2.txt', 'w') as text:
  for i in l:
    text.write(i+' ')

with open('input2.txt', 'r') as abc:
  var = abc.readlines()
  size1 = int(var[0])
  l1 = var[1].strip().split(' ')

  size2 = int(var[2])
  l2 = var[3].strip().split(' ')

  li = []
  i = 0
  j = 0

  while i < len(l1) and j < len(l2):
    #print(i)
    if int(l1[i]) < int(l2[j]):

        li.append(l1[i])
        i+=1
    elif int(l2[j]) < int(l1[i]):

        li.append(l2[j])
        j+=1
  while len(li) != len(l1) + len(l2):
    if i < size1:
      li.append(l1[i])
      i+=1
    if j < size2:
      li.append(l2[j])
      j+=1
with open('output2.txt', 'w') as my_file:
  for i in li:
    my_file.write(str(i)+' ')