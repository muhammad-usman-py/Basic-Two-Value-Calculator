def calculator(a, operator, b):
    try:
        a = float(a)
        b = float(b)

        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Error: Division by Zero"
            return a / b
        else:
            return "Invalid Operator"
    except ValueError:
        return "Invalid Input"
