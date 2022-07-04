#class Student:
#    def __init__(self, name, id):
#        self.name=name
#        self.id=id
            
#    def print(self):
#        print(self.name)
#        print(self.id)    

#p1=Student("Ivan", 221)
#p2=Student("Mitko", 222)
#p1.print()
#print()
#p2.print()

##2 просто не искаше да работи
#import numbers
#class Myclass:
#    def __init__(self,list):
#        self.list=[]
#        
#    def add(self,num):
#        for i in range(len(list)):
#            try:
#                l1=float(list[i])
#                self.list.append(l1)
#            except ValueError:
#                pass


#    def print(self):
#        print(self.list)
#    #def average(self):
#    #    return sum(self.list)/len(self.list)

#l2=[1,2,3,'a',6,'b','c']
#l1=Myclass(l2)
#l1.print()
##l1.average()

#2 raboti
#class Myclass:
#    def __init__(self,list):
#        self.list=[i for i in list if type(i)==int]
#    def print(self):
#        print(self.list)

#    def avrg(self):
#        print(sum(self.list)/len(self.list))

#l1=[1,4,61,'a','b',5,7,1,]
#num=Myclass(l1)
#num.print()
#num.avrg()

#3
class Myclass:
    def __init__(self,num):
        self.num=num
    def my_func(num_obj):
        obj_list=[]
        for i in range(num_obj):
          obj_list.append(Myclass(i*2+1))
        return obj_list

my_list=my_func(10)

for i in my_list:
    print(i.num)



