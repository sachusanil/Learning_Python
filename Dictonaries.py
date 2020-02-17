spam = {'Bob': 'Oct 12', 'Dylan': 'dec 4'}

while True:
    print("Enter name to check, Blank to Quit")
    name = input()
    if (name !=''):
        if name in spam:
            print('The birthday of '+ name + ' is on '+ spam[name])
        else:
            print('Birthday not in our list')
            print('What is their birthday?')
            bday=input()
            spam[name]=bday
            print('Birthday Updated')
    else:
        print('See you soon')
        break



