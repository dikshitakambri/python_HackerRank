import textwrap

def wrap(string, max_width):
    l= list()
    for i in range(0,len(string),max_width): l.append(string[i:i+max_width])
    return "\n".join(l)


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
    
'''
Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
