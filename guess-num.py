import random

r = random.randint(1, 100)
while True:
	num = input('Please guess the number.')
	num = int(num)
	if num == r:
		print('You are correct!')
		break
	elif num > r:
		print('Too big')	
	elif num < r:
		print('Too small')	