# function that has one argument ( text )


# here is the dictionary of vowels and their match


def replace_vowels(text):
    # empty to create the new text
    vowels = {"a": "6", "e": "3", "i": "1", "o": "0", "u": "b"}

    result = ""
    # the loop starts here and goes over each character
    for char in text:
        # checks for lowercase
        if char.lower() in vowels:
            # result sends it to result if not in dictionary
            result += vowels[char.lower()]
        else:

            # combines the changed  characters
            result += char
    # shows result of function
    return result


def init():
    text = input("Enter some letters here:  ")
    new_text = replace_vowels(text)
    print("Original word:", text)
    print("Modified word:", new_text)


init()
