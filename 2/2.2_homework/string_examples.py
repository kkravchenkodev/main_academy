# Conver the string e.g.  "This is a late parrot"  into camelCase "thisIsALateParrot"
targetString = 'thisIsALateParrot'
a = 'This is a late parrot'
print(a)
S = ''.join([(x[0].lower() if x[0] == x[0].upper() else x[0].upper()) + x[1:] for x in a.split(' ')])
print(S)
print(targetString == S)
print('\n--------------------------------------\n')
s = 'This is a late parrot'
print(s)
x = ''.join(s.title().split())
print(x.replace(x[0], x[0].lower()))
print(targetString == x)
print('\n--------------------------------------\n')

# Replace all o's except first one with $ "Welcome to Python 101 course" -> "Welcome t$ Pyth$n 101 c$urse"
s = "Welcome to Python 101 course"
print(s)
print(s.replace('o', '$').replace('$', 'o', 1))
