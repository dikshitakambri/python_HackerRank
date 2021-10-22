def repeatedString(s, n):
    
    
    count=s.count('a')
    
    length=len(s)
    st=''
    if('a' not in s):
        return 0
    if(length==1):
        return n
    else:
        div=int(n/length)
        rem=n-div*length
        count=count*div+ s[:rem].count('a')
    return count
