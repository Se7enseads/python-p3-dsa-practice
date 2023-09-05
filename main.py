import re


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


def remove_duplicates(sequence):
    seen = []
    result = []

    for item in sequence:
        if item not in seen:
            seen.append(item)
            result.append(item)

    return result


def word_frequency(sentence):
    word_pattern = r'\b\w+\b'

    words = re.findall(word_pattern, sentence.lower())

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
