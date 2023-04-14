# Write a Python function to sum all the numbers
# in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)  
def addition(*numbers):
    answer=0
    for number in numbers:
        answer+=number

    return answer     

# Write a Python function to multiply all the
# numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
       
def multiply(*numerals):
    result=1
    for numeral in numerals:
        result*=numeral

    return result


#form a dictionary  from function that print  sout
#  the attributes of a person

def person_Attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")   
    

# Write a function that takes two numbers 
# as input and returns their sum.
def sum(*digits):
    answer1=0
    for digit in digits:
        answer1+=digit

    return answer1  


#Write a function that takes a list of numbers as 
# input and print the average of the numbers.
def average(*counts):
    average=sum(counts)/len(counts)
    
    print("Average of list",round(average,1))
    
        



       

        





