## FOR LOOPS
names = ['Marie', 'Pearl', 'Yaa', 'Nono', 'Akoto']

for name in names:
    print("One of her names is: " + name)
for name in names[0:2]:
    print("And her first name is: " + name)

##WHILE LOOPS
age =int(input("How old are you?: "))
num = 18

while age < num:
    print("Sorry you are unable to vote this year.")
    age +=1

## RANGES:
#LEAP YEAR CALCULATOR (ONLY WORKS FOR EVEN NUMBERS)
start = int(input("What is the starting year?: "))
end = int(input("What is the ending year?: "))

count = 0
for year in range(start,end,4):
    count +=1 
print (count)
