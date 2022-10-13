from operator import pow, sub, mul, add, truediv

def calculate(voice_input):
    operators = {
        '+': add,
        '-': sub,
        '/': truediv,  # floordiv also exists, which is integer division
        'x': mul,
        '^': pow
    }
    for symbol, operator in operators.items():
        if symbol in voice_input:  # Check if the symbol is in the string
            a, b = voice_input.split(symbol)
            print (operator(float(a), float(b)))  # Cast them to floats - all builtin operators can handle them.
