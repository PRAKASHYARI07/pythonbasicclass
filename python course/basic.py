# this is string
# first_name = "prakash"

# #this is integer
# number=12

# # this is float
# ram=12.00

# this is boolean
# is_this_right=True

# num1=100
# num2=200
# print(num1+num2)
# print(first_name)
# print(number)
# print(ram)
# print( type(first_name))


# #to take user input

# user_name=input('what is your name')
# user_age=input('what is your age')
# print('your name is'+ str(user_name))
# print('your age is',user_age)


# writing a program  to create a app that calculate user age by itd date of birth

# year_birth=input('enter your of bith')
# current_year=2024
# current_age= (current_year) - int(year_birth)
# print( 'your age is', (current_age)) 




# condition 

# if current_age <=21:
#     print('you r prakash yari')

# else:
#     print('you r hero')
    




# it is just for the dtudent scholarshipp

# user_name=input('what is your name')
# user_per=input('enter your percentage')
# if  int(user_per)>=80:
#     print('you got a first division')
# else:
#     print('you just passed')



# user input

# while True:
#     name=input('what is your name ')
#     percentage=input('enter your percentage')
    
    
# print(name)
# print(percentage)






# logical operator
# is_hency=True
# is_beautiful=False
# if is_hency or is_beautiful:
#     print('you r at the list of world mrs.')
# else:
#     print('you r not selected')



# # comparison operator
# Temperature=input('enter your area temperature')
# if  int(Temperature)>=30:
#     print('its a hot day')
# elif int(Temperature)>=20:
#     print('its a cold day')
# else:
#     print('its neither hot nor cold')



# check even or odd number 

# num1=input('enter your number')
# if int (num1)%2==0:
#     print('this is even number')
# else:
#     print('this is odd number')
    
    
    
# LOOPS
# for i in range(1,1000):
#     if i==500:
#         print('i have got the righrt answer')
#         break
#     print(i)



# * loopss

# for i in range(1,6):
#     print('*'*i)




# lists in python


# fruits_list=['mango','apple','banana','grapes']



# while True:
#     new_fruits=input('Enter the new fruits bought in department:')
#     fruits_list.append(new_fruits)
#     print('after appending')
#     print(fruits_list)


# while True:
#     rem_fruits=input('enter the fruits you want to remove')
#     fruits_list.remove(rem_fruits)
#     print('after removing')
#     print(fruits_list)

# for x in range(5):
#     for y in range(3):
#         print(f'({x},{y})')


# numbers=[4,3,2,1]
# for x_count in numbers:
#     print('x'* x_count)



# dictionary


# car_info={
#     'modal':'2000',
#     'color':'red',
#     'prize':'120000$'
# }

# for i in range(3):
#  print('what do u want to insert')
#  key_value=input('enter the key')
# value_name=input('enter the value')
# car_info.update(
#     {
#         'type':value_name
#     }
# )
# print(car_info)




# STRING operation in  PYTHON


# str_name='prakash yari'
# print(str_name)
# print(len(str_name))


# car_list=['ford','suzuki','Ev']
# print(car_list)
# print(car_list[1])

# #for slicing string
# ######################################
# example= "Favourite fruit is mango"
# if 'mango' in example:
#     print("yes, mango is favourite")

# #slicing
# print(example[2:8])  

# print(example[-5:-1])

# print(example[:10])

# print(example[2:])
# ######################################
# print(car_list[1:2])
# #####################################




# #remooving the white spaces 
# new_s=(  ' i  am so lucky laaa!!')
# print(new_s.strip())
# print(new_s.replace('i','p'))

# SPLITTING THE STRING


# split_name='prakash12yari'
# print(split_name.split('12'))


# CONCATINATION THE STRING



# name1='prakash'
# name2='yari'
# concate_name=name1+"   "+name2
# print(concate_name)

# def sum(a,b):
#     sum=a+b
#     return sum
# print('the sum of 10 and 20 is :' ,sum(10,20))



#FUNCTION IN PYTHON

#########################





 ####################   FUNTION IN PYTHON ###############################
 
 
 
# def greet():
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

# #default value function

# def defaultvaluefunction( country='nepal',city='kathmandu'):
#     print('your country name is :',country)
#     print('your city name is :',city)
    
# defaultvaluefunction()
    








