# class Student:
#     def __init__(self):
#         self.name = input("What is your name?")
#         self.degree = input("What is your degree type?: ")
#         self.course = input("What is your course of study?")
#         self.sex = input('What us your sex?')

# student1 = Student()
# print(f'This {student1.degree} {student1.sex} student is called {student1.name} and studies {student1.course}')


#BMI CALCULATOR
# class Person:
#     def __init__(self):
#         self.height = input("Enter your height in cm:  ") 
#         while type(self.height)!= float:
#            print('Invalid input for height')
#            self.height = input("Enter your height in cm:  ") 


#         self.weight = float(input("Enter your weight in kg: "))
#         height_meters = self.height / 100
#         self.bmi = float(self.weight /(height_meters ** 2))

#         print(f'Your BMI is {self.bmi:.1f}')

#         if (self.bmi < 18.4 and self.bmi == 18.4):
#             print("You are underweight.")
#         elif  (self.bmi > 18.4 and  self.bmi < 24.9):
#             print("You are of normal weight.")
#         elif(self.bmi > 25 and self.bmi < 40):
#             print("You are overweight.")
#         else:
#             print("You are obese.")


#         return None

# Person1 = Person()

# def inputF():
#     while True:
#         try:
#             height =float( input("Enter your height in cm:  ") )
#             if height <= 0:
#                 print("Enter positive number")
#                 continue
#             break
#         except ValueError:
#             print("Invalid input for height.")
        
#     while True:
#         try:
#             weight = float(input("Enter your weight in kg: "))
#             if weight <= 0:
#                 print("Invalid input for weight.Enter postive number:")
#                 continue
#             break
#         except ValueError: 
#             print("Invalid input for weight.")

                 
#     print(f'Height: {height}cm and weight is: {weight}kg')

#     height_meters = height / 100
#     bmi = float(weight /(height_meters ** 2))

#       print(f'Your BMI is {self.bmi:.1f}')

#       if (self.bmi < 18.4 and self.bmi == 18.4):
#            print("You are underweight.")
#     elif  (self.bmi > 18.4 and  self.bmi < 24.9):
#            print("You are of normal weight.")
#       elif(self.bmi > 25 and self.bmi < 40):
#              print("You are overweight.")
#          else:
#              print("You are obese.")


# def bmi():


# try:
#     float("k")
# except ValueError as mistake:
#     print("Error:",mistake)

## ONE FUNCTION BMI CALCULATOR:
def bmi_calculator():
    name = input("Hi there! Enter your name to proceed: ")
    while True:
        try:
            height =float( input("Enter your height in cm:  ") )
            if height <= 0:
                print("Enter positive number")
                continue
            break
        except ValueError:
            print("Invalid input for height.")
        
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                print("Invalid input for weight.Enter postive number:")
                continue
            break
        except ValueError: 
            print("Invalid input for weight.")

                 
    print(f'Okay {name}, your height is {height}cm and weight is {weight}kg')

    height_meters = height / 100
    bmi = float(weight /(height_meters ** 2))

    print(f'Your BMI is {bmi:.1f}')

    if (bmi < 18.4 and bmi == 18.4):
        print("You are underweight.")
    elif  (bmi > 18.4 and  bmi < 24.9):
        print("You are of normal weight.")
    elif(bmi > 25 and bmi < 40):
        print("You are overweight.")
    else:
        print("You are obese.")

bmi_calculator()