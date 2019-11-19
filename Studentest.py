def sum13(numbers):
    if len(numbers) == 0:
        return 0

    for i in range(0, len(numbers)):
        if numbers[i] == 13:
            numbers[i] = 0
            if i+1 < len(numbers): 
                numbers[i+1] = 0
    return sum(numbers)

print("The total is: ")
print(sum13([1, 2, 2, 12, 13, 45]))