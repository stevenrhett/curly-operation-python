alphabet = "abcdefghijklmnopqrstuvwxyz"


def rotate(message, n):
    encrypted_message = ""
    for char in message:
        if char.lower() in alphabet:
            old_index = alphabet.index(char.lower())
            new_index = (old_index + n) % 26
            if char.isupper():
                encrypted_message += alphabet[new_index].upper()
            else:
                encrypted_message += alphabet[new_index]
        else:
            encrypted_message += char
    return encrypted_message


message = "hello"
print("Original message:", message)
for n in range(1, 10):
    encrypted_message = rotate(message, n)
    print("Encrypted message rotation",n, ":",  encrypted_message)



# def rotate(message, n):
#     encrypted_message = ""
#     for char in message:
#         if char.lower() in alphabet:
#             old_index = alphabet.index(char.lower())
#             new_index = (old_index + n) % 26
#             new_char = alphabet[new_index]
#             if char.isupper():
#                 new_char = new_char.upper()
#
#             encrypted_message += new_char
#         else:
#             encrypted_message += char
#     return encrypted_message
#
#
# message = "hello"
# n = 1
# encrypted_message = rotate(message, n)
# print("Original message:", message)
# print("Encrypted message:", encrypted_message)
