#операции при кортежи

k=(7,5,3,6,1)
print(k[0]) #достъп до елемент по индекс
print(k[2:3])   #сечение
print(7 in k)   #проверка на наличие на елемент
print(k*3)  #повторение
tup=k+(2,4) #конкатенация/събиране
print(tup)

#проддържани методи при кортежите

tup=(7,5,3,6,1)
print(tup.index(1)) #4
print(tup.index(5)) #1

#обхождане на елемнетите на кортеж
for i in tup:
    print(i,end='')

#създаване на речник
d=dict()
d1=dict(name='ivan', last_name='petrov')
d3=dict([('name','polina'),('l_name','koleva')])
print(d3)
print(d1)

#запълване на речник елемент по елемент
d={}
d['name']='petyr'
d['l_name']='kolev'
d={'name':'ivan','last_name':'ivanov'}
print(d)

#операции с речници
d={'name':'ivan', 'last_name':'ivanov'}
d['name']
# print(d['fname']) #KeyError; 'fname'

#проверка за наличие на ключ
b='fname' in d
print(b) #false

#определяне броя на ключовете в речника
len(d)
print(len(d)) #2

#добавяне на елементи в речника
d['s_name']='petrov'
print(d) #(name':'ivan','last name'; 'ivanov'

#премахване на елемнт от речник- използва се оператора del
del d ['s_name']
print (d) #('name':'ivan', 'last_name'; 'ivanov')

#методи keys() i values()
keys=list(d.keys())
keys.sort()
for key in keys:
    print("(0)=>(1)".format(key, d[key]), end='')
        #last_name=>ivanov name=>ivan

#множества
s=set([1,2,3,1])    #list
print(s)
s2=set("hello")     #string

#-функция len()
#print(len(s2) #4

#операции с множества
#обхождане на множество
s2=set("hello")
for i in s2:
    print(i,end='') # l h e o

#-обединение на множества
s=set([1,2,3])
s1=set([4,2,6])
s3=s|s1
print(s3)

#разлика на множества
s=set([1,2,3,4])
s1=set([2,4,6])
s2=s-s1
print(s2) #1.3
s3=s1-s
print(s3) #6

#пресичане на множества
s=set([1,2,3,4])
s1=set([2,4,6])
s4=s&s1
print(s4) #(2.4)

#operator ^
s=set([1,2,3,4])
s1=set([2,4,6])
s5=s^s1
print(s5) #1,3,6
    

#методи на множествата
#add(<element>)
#remove(<element>)
#discard(<element>)
#pop()
#clear()
s1=set([2,4,6])
s1.add(8)
s1.remove(2)
print(s1)
#s1.remove(2) #keyError: 2