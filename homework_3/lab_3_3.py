import math
import random

"""
Generate sequence 5 integers long from range(0, 100)
• Generate random float
• Print variables above
• Find max element from generated sequence
• Make a floor division between max element and generated float
• Find factorial of the result above
• Shorten the code as much as possible
"""
int_seq = [random.randint(0, 100) for i in range(5)]
float_random = random.random()

print(*int_seq)
print(float_random)

int_seq_max = max(int_seq)
print(int_seq_max)

floor_div_result = int_seq_max // float_random
print(floor_div_result)
print(math.factorial(int(floor_div_result)))
