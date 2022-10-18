def start_calculator():
    print("Robot Calculator Started")


def calculate_term(term):
    """
    Interpret term as a mathematical expression
    and return the result
    """
    print("Robot Calculating Term:", term)
    return eval(term)
