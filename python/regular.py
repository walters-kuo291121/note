import random


#generate random number of length
def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)

print(randN(5))
print(randN(7))
print(randN(4))
print(randN(8))


