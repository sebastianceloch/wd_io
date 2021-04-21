numbers = [i for i in range(1, 25 + 1)]
print(numbers)
numbers_two_level = [numbers[i * 5:i * 5 + 5] for i in range(int(len(numbers) / 5))]
print(numbers_two_level)
print(numbers_two_level[0][0])