def array_diff(a, b):
    result = []
    for element in a:
        if element not in b:
            result.append(element)
    return result

a = [1, 2, 3]
b = [1, 2]
result = array_diff(a, b)
print(result)
