from config import MATH_MODE_EQUATION

def create_pattern_function(expr: str=MATH_MODE_EQUATION):
    expr = expr.replace("^", "**")  # Support ^ as exponent
    def pattern(n):
        try:
            return eval(expr, {"n": n, "math": math})
        except Exception as e:
            print("Error in pattern:", e)
            return 0
    return pattern

def func(n, pattern_func):
    value = pattern_func(n)
    rounded = round(value)
    index = (rounded - 1) % 6
    return functions[index]()
