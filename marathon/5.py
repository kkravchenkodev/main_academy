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

import re


def toPostFixExpression(e):
    # divide string into tokens, and reverse so I can get them in order with pop()
    # tokens = re.split(r' *([\+\-\*\^/]) *', e)
    # print(tokens)
    tokens = [t for t in reversed(e) if t != '']
    print(tokens)
    precedence = {'+': 0, '-': 0, '/': 1, '*': 1, '(': 2, ')': 2}

    # convert infix expression tokens to RPN, processing only
    # operators above a given precedence
    def to_rpn(tokens, minprec):
        rpn = tokens.pop()
        while len(tokens) > 0:
            prec = precedence[tokens[-1]]
            if prec < minprec:
                break
            op = tokens.pop()

            # get the argument on the operator's right
            # this will go to the end, or stop at an operator
            # with precedence <= prec
            arg2 = to_rpn(tokens, prec + 1)
            rpn += arg2 + op
        return rpn

    return list(to_rpn(tokens, 0))





print(toPostFixExpression(["2", "+", "3"]))
print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))
