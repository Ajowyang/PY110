numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1
print(numbers) #[2, 2, 3, 4]
for i in range(1, len(numbers)):
    numbers[i] = numbers[i] + 1
print(numbers)
numbers[4] = numbers[4] + 1 #IndexError: list index out of range
