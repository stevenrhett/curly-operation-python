def replace_vowels(text):
    vowels = {"a": "6", "e": "3", "i": "1", "o": "0"}
    result = ""
    for char in text:
        if char.lower() in vowels:
            result += vowels[char.lower()]
        else:
            result += char
    return result


text = input("Enter some text: ")
new_text = replace_vowels(text)
print("Original text:", text)
print("Modified text:", new_text)
