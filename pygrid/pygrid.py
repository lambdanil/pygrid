import os

# Clears the screen
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

# Create grid
def makegrid(x,y):
	maxchars = x*y
	chars = 0
	grid = []
	while chars != maxchars:
		grid.append("#")
		chars+=1
	return grid

# Pring the grid
def printgrid(grid,x,y):
	looped = 0
	# Add numbers to top
	toprint = 1
	toprintstr = "  "
	while toprint != x+1:
		if toprint < 10:
			toprintstr = toprintstr + str(" ") + str(toprint)
		else:
			toprintstr = toprintstr + str("") + str(toprint)
		toprint+=1
	print(toprintstr)
	#-------------------
	while looped != y:
		newgrid = []
		while len(newgrid) != x:
			newgrid.append(grid[len(newgrid)+(x*looped)])
		# Add numbers to side
		if len(str(int(looped+1))) < 2:
			print(looped+1, "", " ".join(newgrid))
		else:
			print(looped+1, " ".join(newgrid))
		#--------------------
#		print("".join(newgrid))
		looped += 1

# Write to grid
def write(grid,x,y,add):
	add1, add2 = add.split("|")
	add1,add2 = int(add1),int(add2)
	if add1 > (len(grid) / y):
		print("Error")
	elif add2 > (len(grid) / x):
		print("Error")
	else:
		toadd = add1+((add2-1)*x)
		grid[toadd-1] = "."
		print(grid)
		return(grid)

clear()
print("Enter grid height:")
grid_h = int(input("> "))
print("Enter grid width:")
grid_w = int(input("> "))
grid = makegrid(grid_w,grid_h)
while True:
	clear()
	printgrid(grid,grid_w,grid_h)
	print("Add point to: (x|y)")
	addto = str(input("> "))
	grid = write(grid,grid_w,grid_h,addto)
