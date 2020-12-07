import random
from collections import Counter

numbers = [random.randint(0, i) for i in range(25)]
print(numbers)
counter = Counter(numbers).most_common()
print(counter)

