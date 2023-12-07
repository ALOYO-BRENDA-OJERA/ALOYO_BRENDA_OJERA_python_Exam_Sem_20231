#NUMBER ONE (i)
import math
class Calculate_area:
    def __init__(self,radius):
     self.radius=radius
    def area_of_a_circle(self):
        area= math.pi*self.radius**2
        return area
#creating an instance of calculate area
circle = Calculate_area(5)
area = circle.area_of_a_circle()
print(area)






#(ii)

def sum_of_natural_numbers_up_to_n(n):
    sum=0
    for i in range(1, n+1):
        total_sum +=i
    output= total_sum
print(i)
# testing usability
numbers = 5
result = sum_of_natural_numbers_up_to_n(numbers)



#(iii)
numbers=[1,3,5,7,9]
new_number = numbers.pop(2)
print(new_number)

 
 
#(iv)
even_numbers=[2,4,6,8,10]
print((even_numbers) for i in even_numbers:if i %2==0)

 
 
#iv)
student_info={
    'name':'Alice',
    'age':'20',
    'grade':'A'
}
#updating the value for age.
student_info['age'] = 25
print(student_info)

#adding a new key value 
student_info['city']= 'newyork'
print(student_info)

# 
original_dict = {'a': 3,
                 'b': 8,
                 'c': 2, 
                 'd': 7
                 }
new_dict = {key: value for key, value in original_dict.items() if value > 5}
print(new_dict)



  
    



    