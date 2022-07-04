class Person:
    def __init__(self, name, family, age, nationality):
        self.name=name
        self.age=age
        self.family=family
        self.nationality=nationality

    def print(self):
        print(self.name)
        print(self.family)
        print(self.nationality)



class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age,nationality )
        self.university=university
        self.yearofstudy=yearofstudy


p1=Student("Ivan", "Ivanov", "20", "Bulgarian","Technical University", '2021')
p2=Student("Mitko", "Mitev", '21' , "Macedonian", "University of Sofia", '2019')

print(p1.name +" "+ p1.family+" is "+ p1.nationality + " " + p1.age +" and he is studying in " + p1.university + " from " + p1.yearofstudy)
print(p2.name +" "+ p2.family+" is "+ p2.nationality + " " + p2.age +" and he is studying in " + p2.university + " from " + p2.yearofstudy)

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university=university
        self.experience=experience
        
l1=Lecturer("Georgi", "Georgiev", "41", "Bulgarian", "Technical University", "15")
l2=Lecturer("Mariq", "Georgieva", "38", "Bulgarian", "Technical University", "10")

print(l1.name +" "+ l1.family+" is "+ l1.nationality + " " + l1.age +" and he is teaching in " + l1.university + " from " + l1.experience)
print(l2.name +" "+ l2.family+" is "+ l2.nationality + " " + l2.age +" and she is teaching in " + l2.university + " from " + l2.experience)


