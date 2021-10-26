import numpy

n,m,p=map(int,input().split())

list1=[list(map(int,input().split())) for i in range(m)]
list2=[list(map(int,input().split())) for i in range(n)]
a1=numpy.array(list1)
a2=numpy.array(list2)

print(numpy.concatenate((a1,a2),axis=0))
