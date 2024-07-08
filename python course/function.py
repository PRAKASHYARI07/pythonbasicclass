# # def greet():
# #     print('namaste')
    
# # # greet()
# # def sum(a,b):
# #     sum=a+b
# #     print(sum)
# # sum(10,20)
# # def user_names(fname):
# #     print(f'hi {fname} how r you ?' )
    
# # user_names('prakash')
# # user_names('siddu')
# # user_names('kushal')

# #FUNCTION BASIC


#  #in built function  print(),len(),input()
# # def my_function():
# #     print('this is function')
    
    
# # my_function()
# # #how to perfrom calculator using function

# # def calculated():
# #     num1=30
# #     num2=20
# #     num3=10
# #     multiply=num1*num2*num3
# #     print(multiply)
    
# # calculated()  

   
# #RETURN FUNCTION

# # def claculate():
# #      num1=20
# #      num2=30
# #      return num1+num2
# # sum_data = claculate()
# # print(sum_data)
     
     
# #PARAMETER FUCNCIOn
# # def parameterfun(num1,num2,num3,name):
# #     print(num1)
# #     print(num2)
# #     print(num3)
# #     print(name)
    
# # parameterfun(12,13,14,'prakash ')
    
# #how to perform operation inside the parameter functionn

# # def parafunction( naming,year):
# #     print('the user name is',naming)
# #     current_year=2024
# #     real_age=current_year-int(year)
# #     return real_age
 
# # name=input('enter your name :')
# # age=input('enter your age:')

# # real_birth_age=parafunction(name,age)
# # print(real_birth_age)


# # # # HOW TO HANDLE ARBITARY ARGUMNETS
# # def arbfunction(*args):
# #     selected_user = ['ram','prakash']
# #     print(args)
# #     for i in args:
# #         print(i)
# #         if i in selected_user:
# #            print('selected user found!',i)
        
        
# # arbfunction ('sid','prakash','kushal', 10,20,30)
    
# # #how to handle keyword argument

# # def keyfunction( **kwargs):
# #     print(kwargs)
# # keyfunction(name1='prakash' ,name2='kushal')


 ################## #            default value function  ###############


# def defaultvaluefunction( country='nepal',city='kathmandu'):
#     print('your country name is :',country)
#     print('your city name is :',city)
    
# defaultvaluefunction()


                       #HOW TO ACCES THE GLOBAL VARIABLE 
                       
                       
# street='jorpati'
 
# def globalchangefun():
#     global street
#     street='chabel'
#     print(street)
# globalchangefun()
# print(street)