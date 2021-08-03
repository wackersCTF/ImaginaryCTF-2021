import numpy
import binascii

message = open("info.txt","r")
message = str(message.read())
#print(message)
messageDigest = message.split(" ")
#initial state: 1/sqrt(2)*(|00> + |11>)

X = numpy.array([[0, 1], [1, 0]])
I = numpy.array([[1, 0], [0, 1]])
Z = numpy.array([[1, 0], [0, -1]])
ZX = numpy.dot(Z, X)
H =  numpy.array([[1, 1], [1, -1]])
CNOT = numpy.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

XI = numpy.kron(X, I)
II = numpy.kron(I, I)
ZI = numpy.kron(Z, I)
ZXI = numpy.kron(ZX, I)
HI = numpy.kron(H, I)

init1 = numpy.array([1, 0, 0, 0])
init2 = numpy.array([0, 0, 0, 1])

initial = (1 / 2 ** (1 / 2) * (init1 + init2))
digest = ""
for m in messageDigest:
    if m == "I":
        init1 = numpy.transpose(numpy.dot(init1,II))
        init2 = numpy.transpose(numpy.dot(init2,II))
    elif m == "X":
        init1 = numpy.transpose(numpy.dot(init1,XI))
        init2 = numpy.transpose(numpy.dot(init2,XI))
    elif m == "Z":
        init1 = numpy.transpose(numpy.dot(init1,ZI))
        init2 = numpy.transpose(numpy.dot(init2,ZI))
    elif m == "ZX":
        init1 = numpy.transpose(numpy.dot(init1,ZXI))
        init2 = numpy.transpose(numpy.dot(init2,ZXI))
    else:
        print("Unknown Op: {0}".format(m))

    dig1 = numpy.transpose(numpy.dot( init1,CNOT))
    dig2 = numpy.transpose(numpy.dot(init2, CNOT))
    dig1 = numpy.transpose(numpy.dot(dig1,HI))
    dig2 = numpy.transpose(numpy.dot(dig2,HI))
    dig = dig1 + dig2
    if dig[0] != 0:
        digest += "00"
    elif dig[1] != 0:
        digest += "01"
    elif dig[2] != 0:
        digest += "10"
    elif dig[3] != 0:
        digest += "11"
n = int('0b'+digest,2)

#x = n.to_bytes()
x = n.to_bytes((n.bit_length() + 7)//8,'big')#.decode())
x = x.decode("utf-8","ignore")
print(x)
'''
path = "bytes.txt"
with open(path, encoding="utf8", errors='ignore') as f:
    print(f.read())
'''
'''
for i in range(9):
    try:
        print(n.to_bytes((n.bit_length() + i)//8,'big'))#.decode())
    except:
        print("failed on i: " + str(i))
'''
