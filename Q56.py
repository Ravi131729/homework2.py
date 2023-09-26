

def compute_division():
    try:
        result = 5 / 0
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except Exception as e:
        return f" error : {e}"

result = compute_division()
print(result)
