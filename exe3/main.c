#1
#text = input("Enter text")
#d1 = dict()
#for i in range(len(text)):
#    if text[i] in d1:
#        d1[text[i]] += 1
#    else:
#        d1[text[i]] = 1
        

#print(d1)

#1.1
#text = input("Enter text: ")
#d1 = dict()
#for i in text:
#    d1[i]=text.count(i)
  
#print(d1)


#2
n=int(input("enter value for n: "))
s1 = list()
for i in range(0,n): 
    s1.append(i)

s2 = list(s1)
s2.reverse()

d = dict()
for i in range(n):
    d[s1[i]] = s2[i]
print(s1)
print(d)

