#to define class we use class and its name
# class mycollege:
#     x='prakash'
# obj=mycollege()
# print(obj.x)

                       #this is how we create class with constructor


# class Classwithcons:
#     def __init__(self) -> None:
#        print('this is being clalled when initzing object')
# obj1=Classwithcons()


#                    this is how we pass parameter (data ) to class


# class classwithdata:
#     def __init__(self,name,address) :
#         self.name= name
#         self.address=address
#         print(self.name)
#         print(self.address)
        
# obj2=classwithdata('prakash ','maitidevi')


#                      this is how we add multiple data in class


# class multiple_funcclass:
#     def __init__(self,name,address,age):
#         self.name=name
#         self.address=address
#         self.age=age
#     def printname(self):
#         print(self.name)
#     def printage(self):
#         print(self.address)
#     def printaddress(self):
#         print(self.age)
# obj3=multiple_funcclass('prakash',21,'maitidevi')
# obj3.printname()   
# obj3.printage()   
# obj3.printaddress()   

        # making simple calculator
import math

class calculator:
    def __init__(self,num):
        self.number=num
        self.splited_data=0
        self.total_amount=0
        print(self.number)
        
    def sumfunction(self):
        self.total_amount= int(self.splited_data[0]) + int(self.splited_data[1])
        print(self.total_amount)
        
    def subfunction(self):
        self.total_amount= int(self.splited_data[0]) - int(self.splited_data[1])
        print(self.total_amount)
        
    def multiplyfunction(self):
        self.total_amount= int(self.splited_data[0]) * int(self.splited_data[1])
        print(self.total_amount)
    def sqrtfunction(self):
        self.total_amount= math.sqrt(float(self.number.split('^'[1])))
        print(self.total_amount)
        
    def splitfunction(self):
        if '+' in self.number:
            # print(self.number.split('+'))
            self.splited_data=self.number.split('+')
            # print(self.splited_data)
            self.sumfunction()
        elif '-' in self.number:
            self.splited_data=self.number.split('-')
            self.subfunction()
        elif '*' in self.number:
            self.splited_data=self.number.split('*')
            self.multiplyfunction()  
        elif '^' in self.number:
            self.sqrtfunction()   
        
while True:
    user=input('enter a number with to calculate')
    obj4=calculator(user)
    print(obj4.splitfunction())


#                    inheritance in class 

# class parentsclass:
#     def __init__(self,name):
#         self.name=name
#         self.class_type ='BIT'
#         print('this is parent class')
#     def printname(self):
#         print(self.name)
        
#       #now inherient the parent class
# class childclass(parentsclass):
#      pass
# obj1=childclass('prakash')
# print(obj1.class_type)
# obj1.printname()
 
