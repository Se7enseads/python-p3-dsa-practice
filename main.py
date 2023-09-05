def remove_duplicates(sequence):
    seen = []
    result = []

    for item in sequence:
        if item not in seen:
            seen.append(item)
            result.append(item)

    return result


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
# print(result)


def is_balanced(expression):
    stack = []
    dictionary = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in dictionary:
            value = stack.pop()
            if dictionary[char] != value:
                return False
        else:
            stack.append(char)

    return not stack
