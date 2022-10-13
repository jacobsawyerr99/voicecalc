import operator

def get_operator(operand):
    return{
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul
    } [operand]

def eval(num1, operand, num2):
    num1, num2 = int(num1), int(num2)
    return get_operator(operand)(num1, num2)
