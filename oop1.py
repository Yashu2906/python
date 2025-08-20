class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Average of ",self.name,"is",sum/3)
        

s1 = Student("Yash" , [89,78,76])
s1.get_avg()

