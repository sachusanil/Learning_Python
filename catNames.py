catnames=[] #variable to store the name of the cats

def addCatName(): # function to add cat names
	global catnames #accessing the global variable
	while True:
		print('Enter name of the cat or Press enter without a value go back')
		name=input()
		if name !='':
			catnames=catnames+[name]
		else:
			break

def chkName(): #function to check cat names
	global catnames
	print('Enter a name to check')
	namechk=input()
	if namechk in catnames:
		print('The name \''+namechk+'\'is in the list')
	else: 
		print('The name \''+namechk+'\'is not in the Directory')
	

def seeName(): # function to see all names
	global catnames
	if (catnames !=[]):
		print('We have the following cats in our list')
		print(catnames)
	else:
		print('We don\'t have any names')


#Main Program
while True:
	print('')
	print("Welcome to Cat Directory!")
	print("Please select an option")
	print('1. Enter Cat Names 2. Search for Cat Names, 3. See all the names, 4. Quit')
	try:
		option = input()
		if (int(option) == 1):
			addCatName()
		elif (int(option)==2):
			chkName()
		elif(int(option)==3):
			seeName()
		elif(int(option)==4):
			break
		else:
			print("Enter 1, 2, 3 or 4")
			continue
	except ValueError:
		print('Enter Digits')
		continue