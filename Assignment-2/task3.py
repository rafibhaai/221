with open('input3.txt','r') as fl:

  var = fl.readlines()
  #print(var)
  size = int(var[0])
  lst = []
  l = []
  for i in range(1,size):
    i = var[i].strip().split(' ')
    i = tuple(i)
    a , b = i
    lst.append(i)
    l.append(b)

  def bubble_sort(arr1,arr2):
    for i in range(len(arr1)):

      for j in range(len(arr1)-i-1):

        if int(arr1[j]) > int(arr1[j+1]):
          arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
          arr2[j], arr2[j+1] = arr2[j+1],arr2[j]

    return arr1,arr2

  x, y = bubble_sort(l,lst)
  #print(y)
  #print(x)

  c = 0
  l1 = []
  li = []
  for j in range(len(lst)):
    if len(li) == 0:
      li.append(lst[j])
      c+=1
    elif int(li[-1][1]) <= int(lst[j][0]):
      li.append(lst[j])
      c+=1
  l1.append(c)
  result = l1 + li
  #print(result)

with open('output3.txt', 'w') as f:
  for i in result:
    if type(i) == tuple:
      a, b = i
      f.write(a+' '+b+'\n')
    else:
      f.write(str(i)+'\n')