def custom_generator(*args):
    i = 0 if args[0] is None else args[0]
    while i < args[1]:
        yield i
        i += 1 if args[2] is None else args[2]


# gener = custom_generator(10)
# print(gener)
# for i in gener:
#     print(i)

print(range())