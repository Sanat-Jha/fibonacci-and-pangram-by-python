nterms=int(input('no. greater than 0:'))
lst = [0,1]
n = 0
while n<nterms:
    n = lst[len(lst)-1]+lst[len(lst)-2]
    lst.append(n)
lst.pop()
for i in lst:
    print(i)
