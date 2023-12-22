numCubesPerColor = {
	"red": 12,
	"green": 13,
	"blue": 14
}

if __name__ == "__main__":
	file = open("input/cubeGames.txt")
	# file = open("input/easyCubes.txt")
	lines = file.readlines()
	validGameSum = 0
	gamePowerSum = 0
	for line in lines:
		# Get the game ID
		strings = line.split(':')
		gameID = int(strings[0][5:])
		# Split the game
		games = strings[1].split(';')
		possible = True
		minCubesPerColor = {
			"red": 0,
			"green": 0,
			"blue": 0
		}

		for game in games:
			pulls = game.split(',')
			for pull in pulls:
				pull = pull.strip().split(' ')
				numCubes = int(pull[0])
				if numCubes > minCubesPerColor[pull[1]]:
					minCubesPerColor[pull[1]] = numCubes
				if numCubes > numCubesPerColor[pull[1]]:
					possible = False
		if possible:
			validGameSum += gameID
		gamePowerSum += minCubesPerColor["red"] * minCubesPerColor["green"] * minCubesPerColor["blue"]
	
	print("Some of those games were possible! Now I'm going to say a number! " + str(validGameSum))
	print("Wow, those were some powerful games! Uhhh " + str(gamePowerSum))
