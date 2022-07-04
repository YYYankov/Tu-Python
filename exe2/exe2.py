n=int(input("Enter n: "))
list1=list()
list2=list()

for i in range(n):
    num=int(input())
    if num%2==0:
        list1.append(num)
    elif num%3==0 and num%2!=0:
        list2.append(num)
    
min=min(list2)
max=max(list2)

sum=sum(list1)
avg=sum/len(list1)

print(min)
print(max)
print(sum)
print(avg)
