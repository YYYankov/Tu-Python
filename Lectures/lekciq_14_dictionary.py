tel={}
print(tel)
tel=dict()
print(tel)

tel={'ivan':'123-123','lili':'345-345','maria':'432-213','georgi':'686-696'}
print(tel)
print(tel['ivan'])

del tel['ivan']
print(tel)

print('lili' in tel)
print('ivan' not in tel)

print(list(tel))
print(sorted(tel))


tel=dict([('ivan','123-123'),('lili','345-345'),('maria','432-213'),('georgi','686-696')])
print(tel)

print({x:x**3 for x in(1,3,4,7)}) #dict comprehansion
print({x: x**3 for x in range(11)})

print(dict(ivan='123-123',lili=345,maria=555)) #za prosti stoinosti

#for k,v in tel.items():
    #print('{0}=>{1}', format(k,v))