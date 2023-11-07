# add your code here
substitution = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

plain_text = input("Please enter a sentence: ")
plain_text = plain_text.lower()

secret_text = ""
for char in plain_text:
    if char in substitution:
        char = substitution[char]
    secret_text += char
    
print(secret_text)

# secret_text = ""
# for char in plain_text:
#     if char in alphabet:
#         # char = substitution[char]
#         letter = alphabet.index(char)
#         newLetter = letter + 5
#         print(letter)
#         print(newLetter)
#         print(len(alphabet))
#         print(alphabet[-25])

#         if newLetter > len(alphabet):
#             newLetter = (letter - (len(alphabet)-1)) + (len(alphabet) * -1) + 4
#             print(newLetter)
#             secret_text += alphabet[newLetter]
#         else:
#             secret_text += alphabet[newLetter]
    
# print(secret_text)