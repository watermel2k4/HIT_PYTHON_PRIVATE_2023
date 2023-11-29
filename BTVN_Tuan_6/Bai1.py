def MyMultiple(*a):
    """
        tính tích
    """
    result = 1.0
    for i in a:
        result *= i
    return result

print(MyMultiple(1,2,3,4))
