# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def Area(self):
#         return 22/7 * self.radius ** 2
    
#     def perimiti(self):
#         return 2 * 22/7 *self.radius 
        

# c1 = Circle(28)
# print(c1.Area())
# print(c1.perimiti())




# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showdetails(self):
#         print("Role - ",self.role)
#         print("Department - ",self.department)
#         print("Salary - ",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Manager","computer",60000)

# e1 = Engineer("Yash Patel",20)
# e1.showdetails()




class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,o2):
        return self.price > o2.price 

o1 = Order("Khakhra",50)
o2 = Order("Tea",30)
print(o1 > o2)