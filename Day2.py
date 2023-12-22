numCubesPerColor = {
	"red": 12,
	"green": 13,
	"blue": 14
}

if __name__ == "__main__":
	file = open("input/cubeGames.txt")
	lines = file.readlines()
	validGameSum = 0
	for line in lines:
		# Get the game ID
		strings = line.split(':')
		gameID = int(strings[0][5:])
		# Split the game
		games = strings[1].split(';')
		possible = True
		for game in games:
			pulls = game.split(',')
			for pull in pulls:
				pull = pull.strip().split(' ')
				if int(pull[0]) > numCubesPerColor[pull[1]]:
					possible = False
					break
			if not possible:
				break
		if possible:
			validGameSum += gameID
	print("Some of those games were possible! Now I'm going to say a number! " + str(validGameSum))
