# Name: Angelica Garcia
# Assignment 10.1: Your Own Class
# Description: required to submit a script that includes
# your implementation of a custom class that is based on 
# a real-world object. The script should include your 
# class and a main function that contains a demo program. 
# You are also required to submit a README that includes 
# documentation of your class and instructions to run the 
# demo program.


# class Student
class Student:
    
    # class variable
    count_of_students = 0
    
    # initialzing the data students
    def __init__(self, ID, name):
        # instance variables
        self.__ID = ID
        self.__name = name
        Student.count_of_students += 1
    
    # getter method to get the ID
    def get_ID(self):
        return self.__ID
    
    # getter method to get the name
    def get_name(self):
        return self.__name
    
    # setter method to set the ID
    def set_ID(self, ID):
        self.__ID = ID
        
    # setter method to set the name
    def set_name(self, name):
        self.__name = name
        
    # method to display the information about an object(Student)
    def display_info(self):
        print("Student ID:", self.get_ID())
        print("Student Name:", self.get_name())
        
    # method to print the total number of students
    def print_number_of_students(self):
        print("The total number of students:", Student.count_of_students)



# main function
def main():
    
    # creating two students objects
    s1 = Student(1, 'Juan')
    s2 = Student(2, 'Martin')
    
    print() # for new line

    # printing the ID of s1 using getter method
    print("Student ID of Student 1:", s1.get_ID())
    
    # setting the ID of s1 using setter method
    s1.set_ID(3)
    
    # printing the ID of s1 again using getter method
    print("Student ID of Student 1:", s1.get_ID())
    
    # printing the information about student s1
    print("\n**Info of Student 1**")
    s1.display_info()
    
    print() # for new line

    # printing the ID of s2 using getter method
    print("Student ID of Student 2:", s2.get_ID())
    
    # setting the ID of s2 using setter method
    s2.set_ID(6)
    
    # printing the ID of s2 again using getter method
    print("Student ID of Student 2:", s2.get_ID())
    
    # printing the information about student s2
    print("\n**Info of Student 2**")
    s2.display_info()
    
    print() # for new line

    # printing the total number of students
    s1.print_number_of_students()

    print() # for new line
    
main()
