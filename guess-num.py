import random
start = input('Please choose start from what number.')
end = input('Please choose end at what number.')
start = int(start)
end = int(end)


r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Please guess the number.')
	num = int(num)
	if num == r:
		print('You are correct!')
		print('This is the', count, 'time you guessed.')
		break
	elif num > r:
		print('Too big')	
	elif num < r:
		print('Too small')	
	print('This is the', count, 'time you guessed.')	