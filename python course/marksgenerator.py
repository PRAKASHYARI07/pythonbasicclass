print('t/t/t/t Marks generator')



science=input('enter the marks in science')
social=input('enter the marks in social')
math=input('enter the marks in math')
boilogy=input('enter the marks in biology')
chemistry=input('enter the marks in chemistry')


total_marks=int(science) +int(math)+int(chemistry)+ int(boilogy)+int(chemistry)

print('your total marks is :', str(total_marks))


total_books_marks=300

total_marks_obtained=total_books_marks/total_marks*100
print( 'your total marks is ',int(total_marks_obtained))


if total_marks_obtained >=90:
    print('you got a distriction')
elif total_marks_obtained>=80:
    print('you got first division')
elif total_marks_obtained>=70:
    print('you got second division')


print('t/t/t/t marks generated by texas college')
