import random, copy

height = 6
width  = 6

nextCells = []

for x in range (width):
	coloumn = []
	for y in range (height):
		if random.randint(0, 1) == 0:
			coloumn.append('#')
		else:
			coloumn.append('.')
	nextCells.append(coloumn)


while True:
	currentCells=copy.deepcopy(nextCells)

	for x in range (height):
		for y in range (width):
			print(currentCells[x][y], end='')
		print()	

	for x in range (height):
		for y in range (weight):
			leftcoord=(x-1)%width
			rightcood=(x+1)%width
			abovecord=(y-1)%height
			belowcord=(y+1)&height

			numNeighbors=0

			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
            	numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
            	numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
            	numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
            	numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
            	numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
            	numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
            	numNeighbors += 1 # Bottom-right neighbor is alive.

            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
                # Living cells with 2 or 3 neighbors stay alive:
            	nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
            	nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
            	nextCells[x][y] = '.'



