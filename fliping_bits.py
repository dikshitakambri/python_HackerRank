def flippingBits(n):
    lt=''
    comp_lt=''
    if len(bin(n).replace("0b", ""))<32:
        bi=bin(n).replace("0b", "")
        rem=32-len(bin(n).replace("0b", ""))
        for x in range(rem):
            bi='0'+bi
        lt=bi
    else:
        lt=bin(n).replace("0b", "")
            
            
   
    ones=''
    for y in range(len(lt)):
        if lt[y]=='1':
            ones=ones+'0'
        else:
            ones=ones+'1'
    comp_lt=(ones)
    return int(comp_lt,2)

    
