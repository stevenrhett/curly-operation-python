def find_min_max(numbers):
    if not numbers:
        return None, None
    min_num, max_num = numbers[0], numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num


numbers = [5, 2, 8, 1, 9, 4]
min_num, max_num = find_min_max(numbers)
print("Minimum number:", min_num)
print("Maximum number:", max_num)
