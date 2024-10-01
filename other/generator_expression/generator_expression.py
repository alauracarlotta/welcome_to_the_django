""" def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result

new_numbers = square_numbers([1, 2, 3, 4, 5])

print(new_numbers) """

def square_numbers(numbers):
    # result = []
    for num in numbers:
        yield (num * num)
        # result.append(num * num)
    # return result

new_numbers = square_numbers([1, 2, 3, 4, 5])

""" print(next(new_numbers))
print(next(new_numbers))
print(next(new_numbers))
print(next(new_numbers))
print(next(new_numbers))
print(next(new_numbers)) """

for nums in new_numbers:
    print(nums)

