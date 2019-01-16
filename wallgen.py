

def main():
	wall = generateWall(40, 7, 'wall')
	print(wall)
	

def generateWall(width, height, material):
	wallString = ''

	for battlement in range(0, width//4):
		for thing in range(0, 4):
			if thing < 2:
				wallString += material
			else:
				wallString += ' '*len(material)
		
	wallString += '\n'

	for row in range(0, height):	#Main wall body
		for column in range(0, width):
			wallString += material
		wallString += '\n'
		
	return wallString


if __name__ == '__main__':
	main()