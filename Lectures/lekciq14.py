#li=[1,2,3,4,5,4,6]
#print(li.count(4))
#print(li.count(0))

#print(li.index(3))
#print(li.index(31))

#li.sort(reverse=True)
#print(li)

#li.reverse()
#print(li)

def squares(n):
    square=[]
    for i in range(n):
        square.append(i**2)
    return square

print(squares(11))

square=list(map(lambda x: x**2, range(11)))
print(square)

square=[x**2 for x in range (11)]   #list comprehasion
print(square)

listcomp=[(x,y) for x in [1,2,3] for y in [3,2,1]]
print(listcomp)

listcomp=[(x,y) for x in [1,2,3] for y in [3,2,1] if x !=y]
print(listcomp) 

listcomp=[]
for x in[1,2,3]:
    for y in [3,2,1]:
        if x!=y:
            listcomp.append((x,y))
print(listcomp)

vec=[-4,-2,0,1,2,-25,32]
print([x*2 for x in vec])
print([abs(x) for x in vec]) #abs() izkarva chislata polojitelni

import math
print([str(round(math.pi, i))for i in range( 1,6)])

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print([[row[i] for row in matrix] for i in range(3)])

trans=[]
for i in range(3):
    trans_row=[]
    for row in matrix:
        trans_row,append(row[1])
    trans.append(trans_row)
    print(trans)

a=[-1,1,2,3,4,-4]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a
#print(a)

li=[-1,22,1,-2,4,-5]
for i, v in enumerate(li):
    print(f'{i}=>{v}')

for i in range(1,30,2):
    print(i,end='')
print()


