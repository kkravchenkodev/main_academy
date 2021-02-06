"""
Convert a certain expression like 2+3 to expression in a postfix notation.
The given expression can have one of the following tokens:
a number;
a parenthesis;
    arithmetic operator:
    subtraction (-);
    addition (+);
    multiplication (*);
    devision (/);
    modulo operation (%).
Example:
For expression = ["2","+","3"] the output should be ["2","3","+"].
[execution time limit] 4 seconds (py)
[input] array.string expression
An array of tokes of a valid expression in the standard notation.
[output] array.string
Tokens of the expression in the postfix notation.
"""

# ALGORITHM:
# 1. Print operands as they arrive.
# 2. If the stack is empty or contains a left parenthesis on top, push the incoming
# operator onto the stack.
# 3. If the incoming symbol is a left parenthesis, push it on the stack.
# 4. If the incoming symbol is a right parenthesis, pop the stack and print the
# operators until you see a left parenthesis. Discard the pair of parentheses.
# 5. If the incoming symbol has higher precedence than the top of the stack, push it
# on the stack.
# 6. If the incoming symbol has equal precedence with the top of the stack, use
# association. If the association is left to right, pop and print the top of the stack and
# then push the incoming operator. If the association is right to left, push the
# incoming operator.
# 7. If the incoming symbol has lower precedence than the symbol on the top of the
# stack, pop the stack and print the top operator. Then test the incoming operator
# against the new top of stack.
# 8. At the end of the expression, pop and print all operators on the stack. (No
# parentheses should remain.)

def toPostFixExpression(e):
    class Stack:
        def __init__(self):
            self.items = []
        def isEmpty(self):
            return self.items == []
        def push(self, item):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
        def peek(self):
            return self.items[len(self.items) - 1]
        def size(self):
            return len(self.items)

    precedence = {'*': 3, '/': 3, '%':3, '+': 2, '-': 2, '(': 1}
    op_stack = Stack()
    postfix_list = []

    for t in e:
        if t.isdigit():
            postfix_list.append(t)
        elif t == '(':
            op_stack.push(t)
        elif t == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (precedence[op_stack.peek()] >= precedence[t]):
                postfix_list.append(op_stack.pop())
            op_stack.push(t)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return postfix_list


print(toPostFixExpression(["2", "+", "3"]))
print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))
print(toPostFixExpression(["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))
