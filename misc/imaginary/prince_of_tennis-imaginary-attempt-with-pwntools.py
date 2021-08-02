from pwntools import *
t = remote('chal.imaginaryctf.org', 42015)
data = t.read()


b = True
while b:
    s = str(t.read()).decode("utf-8").replace("'","")
    print(s)
    if(s[0:2] != "(N" and s[0]=="("):
        res = s.strip().replace(" ","").replace("(",")").split(")")[1:-1]
        operation_list = []
        term_list = []
        for i in range(0, len(res)):
            if(i%2==0): # even indices are terms
                t = res[i].split("+")
                term_list.append([int(t[0]),int(t[1][:-1])])# first item is real, 2nd is imaginary    
            else: # odd indices are operators
                operation_list.append(res[i])
        imaginary_part = term_list[0][1]
        real_part = term_list[0][0]
        term_index = 1
        for x in range(len(operation_list)):
            if(operation_list[x]=="+"):
                real_part += term_list[term_index][0]
            else:
                imaginary_part -= term_list[term_index][1]
            term_index+=1
        
        t.send(str(real_part) + "+"+ str(imaginary_part)+"i")
    else:
        t.sendline("") # just sends a new line (basically equal to a return/enter)
        
t.close()
