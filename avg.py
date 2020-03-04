
def average(numbers):
	return sum(numbers) / len(numbers)
	
print(average(list(map(int, input('Please entre numbers:').split(' ')))))
