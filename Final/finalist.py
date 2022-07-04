class Student():
    def __init__(self, f_num, name, family, grade):
        self.f_num = f_num
        self.name = name
        self.f_name = family
        self.grade = grade

    def __str__(self):
        return str.format('{} {}: {}', self.f_num, self.name, self.grade)


class Group:
    def __init__(self, st_list: list):
        self.st_list: list = st_list

    def present(self):
        for st in self.st_list:
            print(str.format("{} {} -> f_num: {}", st.name, st.f_name, st.f_num))
        print()

    def add_new(self, new_st: Student):
        for st in self.st_list:
            if st.f_num == new_st.f_num:
                print('This student is already in the group!!')
                return
        else:
            self.st_list.append(new_st)
            print("Done")

    def remove(self):
        for i in self.st_list:
            if i.grade < 3:
                self.st_list.remove(i)

    def avg_grade(self):
        grades = [st.grade for st in self.st_list]
        return round(sum(grades) / len(self.st_list), 2)

    def get_min_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade)
        return sr_list[0]

    def get_max_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade, reverse=True)
        return sr_list[0]

    def get_equal_grade(self, grade):
        new_set = set()
        for i in range(len(self.st_list)):
            if self.st_list[i].grade == grade:
                new_set.add(self.st_list[i])
        return new_set
        
    def create_new_list(self, file):
        for row in file:
            data_list = row.split(' ')
            self.st_list.append(Student(int(data_list[0]), data_list[1], data_list[2], float(data_list[3])))

    #четен и нечетен фак.№
    def even(self):
        for st in self.st_list:
            if st.f_num % 2 == 0:
                return st
    def odd(self):
        for st in self.st_list:
            if st.f_num % 2 != 0:
                return st       

gr43a = Group([Student(121221146, 'Aleksandar', 'Shopov', 4.80), Student(121221144, 'Aysel', 'Kazalieva', 4.20),
               Student(121221178, 'Miroslav', 'Dilov', 6.00), Student(121221149, 'Ivan', 'Tomov', 3.60),
               Student(121221096, 'Vasil', 'Alendarov', 3.60),Student(121221010, 'Ívan', 'Nikolov', 6.00)])

# gr43a.add_new(Student(121221178, 'Miroslav', 'Dilov', 6.00))
# gr43a.add_new(Student(121221167, 'Yanko', 'Yankov', 6.00))
# gr43a.present()

# успеь
# print(gr43a.avg_grade())
# print(gr43a.get_min_grade())
# print(gr43a.get_max_grade())


print("\n Odd and even")
print(gr43a.even())
print(gr43a.odd())

# еднакъв успех
print("\n Еднакъв успех" )
gr_stud_list = gr43a.get_equal_grade(3.60)
for i in gr_stud_list:
    print(i, end="  ")

gr43a.remove()
