M = int(input())
Mlist = map(int, input().split())
N = int(input())
Nlist = map(int, input().split())

Mset = set(Mlist)
Nset = set(Nlist)

set1 = Mset.difference(Nset)
set2 = Nset.difference(Mset)

final = set1.union(set2)
final = sorted(final)

for i in final:
    print(i)
