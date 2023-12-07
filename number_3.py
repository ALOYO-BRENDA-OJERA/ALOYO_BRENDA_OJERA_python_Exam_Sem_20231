#3(i) a python snippet that asks the user for their age and prints "you are elligible if the age is greater than or equal to 
# 18, othersiswe prints you are not eligible."
age=int(input("please enter your age"))
 
if age>=18:
   print('you are elligible')
else:
   print('you are not eligible')
   
   
   
   
   #(ii)
   def grade_students():
    marks = int(input("Please enter your mark: "))
    
    if marks >= 90 and marks <= 100:
        print("You have scored an 'A'")
    elif marks >= 80 and marks <= 89:
        print("You scored a 'B'")
    elif marks >= 70 and marks <= 79:
        print("You scored a 'C'")
    elif marks >= 60 and marks <= 69:
        print("You scored a 'D'")
    else:
        print("You scored an 'F'")

grade_students()   
       
#testing the function with 85
marks=(85)



#(iv)modifying the code.
def grade_students():
    marks = int(input("Please enter your mark: "))
    marks=int(input("please enter your mark"))
    if marks==str() and marks==float():
        print("invalid input")
grade_students(70.55)
grade_students("hello")




#enhacing the grade students to provide an additional message.
def grade_students():
    marks = int(input("Please enter your mark: "))
    if marks >= 90 and marks <= 100:
        print("You have scored an 'A'")
        print('Excellent')
    elif marks >= 80 and marks <= 89:
        print("You scored a 'B'")
        print('Excellent')
    elif marks >= 70 and marks <= 79:
        print("You scored a 'C'")
        print('Good')
    elif marks >= 60 and marks <= 69:
        print("You scored a 'D'")
        print('Satisfactory')
    else:
        print("You scored an 'F'")
        print('Needs improvement')

grade_students()


#(vi)
#test using a mark of 78.

"""here, the program user can then enter the mark 78, which brings "You scored a 'C'
Good"
"""

        
        
