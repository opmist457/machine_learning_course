def BooleanAND(inputs):
    if not inputs:
        raise ValueError("Input list cannot be empty")

    for i in inputs:
        if i not in (0, 1):
            raise ValueError("Inputs must contain only binary values 0 or 1")

    g = sum(inputs)
    threshold = len(inputs)

    return 1 if g == threshold else 0


def BooleanOR(inputs):
    if not inputs:
        raise ValueError("Input list cannot be empty")

    for i in inputs:
        if i not in (0, 1):
            raise ValueError("Inputs must contain only binary values 0 or 1")

    g = sum(inputs)
    threshold = 1

    return 1 if g >= threshold else 0

try:
    inputs = [0, 0, 1, 0]   # change this to test
    print("AND Output:", BooleanAND(inputs))
    print("OR Output:", BooleanOR(inputs))

except ValueError as e:
    print("Error:", e)
