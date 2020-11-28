test_var = 'hello'
hello_world = """
Hello
world
"""
print(test_var)
print(hello_world)
print("Hello\nworld")
print()
print('Hello', 'world', sep='\n')
print()

for i in range(10):
    print('hello', end=' ')
else:
    print()

print(' '.join(str(test_var) for n in range(10)))
print(f'{test_var + " "}' * 10)
print()
name = input("Enter your name : ")
age = input("Enter you age : ")
print()
print(f'Your name is {name} and you are {age} years old')
print('Your name is {0} and you are {1} years old'.format(name, age))
