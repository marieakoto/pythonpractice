def fruit_description(dictionary):
    for key, val in dictionary.items():
        print(f'The fruit is {key} and it is {val} in colour')


fruit_colours={}

while True:
    fruit = input("Enter fruit name: ")
    colour = input("Enter fruit colour: ")
    fruit_colours[fruit] = colour

    another = input("Enter another fruit of choice? (y/n)")

    if another == 'y':
        continue
    else:
        break

fruit_description(fruit_colours)