import random

def rollDie():
	return random.choice([1,2,3,4,5,6])

def rollN(n):
	result = ''
	for i in range(n):
		result = result + str(rollDie())
	print(result)

def flip(numFlips):
	heads = 0
	for i in range(numFlips):
		if random.choice(('H', 'T')) == 'H':
			heads += 1
	return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
	fracHeads = []
	for i in range(numTrials):
		fracHeads.append(flip(numFlipsPerTrial))
	mean = sum(fracHeads)/len(fracHeads)
	return mean


if __name__ =='__main__':
	#rollN(10)
	print('Mean =', flipSim(100,10000))
	#pylab.show()
