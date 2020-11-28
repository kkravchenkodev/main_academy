def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        try:
            return arg1 / arg2
        except Exception as e:
            return str(e)
    else:
        return f"Неизвестная операция [ {op} ]"


print(arithmetic(10, 0, ':'))
