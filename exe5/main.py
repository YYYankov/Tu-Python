# num = int(input())
# li3, li7 = list(), list()
# while num!=0:
#     if num%3==0 and num%2==0:
#         li3.append(num)
#     if num%7==0 and num%2!=0:
#         li7.append(num)
#     num = int(input())

# sum_li3 = 0
# for i in range(len(li3)):
#     if i %2 !=0:
#         sum_li3 += li3[i]

# li7.sort(reverse=True)
# mult = li7[0] * li7[-1]


n=int(input("Enter n"))
list3=list()
list7=list()
while n!=0:
    if n%3==0 and n%2==0:
        list3.append(n)
    if n%7==0 and n%2!=0:
        list7.append(n)

sumli3=0
for i in range(len(list3)):
    if i%2!=0:
        sumli3+=list3[i]

list7.sort(reverse=True)
mult=list7[0]*list7[-1]

print(list3,list7,mult,sumli3)
