from itertools import *
#from gmpy2 import *
a = b"jctf{not_the_flag}"
b = b"*-*"
#c = max(*map(len, [a, b]))
#print(c)


def x(a,b):
    return bytes(islice((x^y for x,y in zip(cycle(a), cycle(b))), max(*map(len, [a, b]))))
    
def t(x):
    return sum((((x & 28) >> 4) & 1) << i for i, x in enumerate(x))


a = b"jctf{not_the_flag}"
b = b"*-*"
T = t(x(a,b)) | 1
#print(T)

l = 420
flag = 2535320453775772016257932121117911974157173123778528757795027065121941155726429313911545470529920091870489045401698656195217643

def popcount(x): # i am unable to import gymp2 so this should work
    #https://stackoverflow.com/questions/407587/python-set-bits-count-popcount
    return bin(x).count('1')

for _ in range(421337):
    flag = flag << 1

print(flag.to_bytes(52,"little"))
    # simplify time
    #flag = (flag >> 1) | ((popcount(flag & T) & 1) << (l - 1))
    #flag = (flag >> 1) | 1 << 419)
    #flag = (flag >> 1) | 1353842624082429130653522550851115089568572790710847937094960732721983060451965636249987502980536903367866802227247837807116288)
    
    
