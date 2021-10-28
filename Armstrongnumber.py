n=list(map(int, raw_input()))

l=len(n)
sum=0
for i in n:
    sum=sum+pow(i,l)

sum=str(sum)
s=[]
for y in sum:
    s.append(int(y))

if(sorted(n)==sorted(s)):
    print('armstrong')
else:
    print('not armstrong')
