def checkio(data):
    return data[0] + checkio(data[1:]) if data else 0

print(checkio([1, 2, 3]), 6)
print(checkio([1, 2, 3, 4, 5]), 15)
print(checkio([2, 2, 2, 2, 2]), 10)
