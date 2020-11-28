import random

numbers = [random.randint(0, i) for i in range(25)]
print("Initial list:")
print("----------------------------------------------------------------------------------------------------------")
print(numbers)
print("----------------------------------------------------------------------------------------------------------")
random.shuffle(numbers)
print(numbers)
random.shuffle(numbers)
print(numbers)
random.shuffle(numbers)
print(numbers)
random_number = random.choice(numbers)
print(random_number)
