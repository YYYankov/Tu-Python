# n=int(input("Enter n"))
# list3=list()
# list7=list()
# while n!=0:
#     if n%3==0 and n%2==0:
#         list3.append(n)
#     if n%7==0 and n%2!=0:
#         list7.append(n)

# sumli3=0
# for i in range(len(list3)):
#     if i%2!=0:
#         sumli3+=list3[i]

# list7.sort(reverse=True)
# mult=list7[0]*list7[-1]

# print(list3,list7,mult,sumli3)

class Product:
    def __init__(self, brand, id, price, quant):
        self.brand=brand
        self.id=id
        self.price=price
        self.quant=quant

        

class Order:
    
    def __init__(self, order):
        self.order = order
        

    def add_new(self, pr):
        for i in self.order:
            if i.id == pr.id:
                i.quant +=1
        else:
            self.order.append(pr)

def final_pr(self):
        total = 0
        ship_ord_pr = 5
        for i in self.order:
            total += i.price*i.quant
        
        total += total*20/100
        with open("file.txt", 'w') as f:
            f.write(str('Total:' + str(total) + ' Shipping price:' + str(ship_ord_pr)))
