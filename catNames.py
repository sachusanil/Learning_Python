catnames=[]

while True:
	print('Enter name of the cat')
	name=input()
	catnames=catnames+[name]

	if name =='':
		break
print('The names of my cats are: ', end='')
print(catnames)