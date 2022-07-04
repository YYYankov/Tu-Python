s=set()
print(s,len(s))
s={1,2,3,5,11,-2}
print(s,len(s))
s1=set([4,5,6,1])
print(s1,len(s1))

print({x for x in s1 if x>=2})  #set comprehension
