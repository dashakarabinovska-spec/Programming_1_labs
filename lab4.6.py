a = input()
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []
word = ""
for letter in a:
    if letter.lower() in b:
        word += letter
    else:
        if word != "":
            words.append(word)
            word = ""
if word != "":
    words.append(word)
k = max(len(word) for word in words)
result = ""
for letter in a:
    if letter.lower() in b:
        i = b.index(letter.lower())
        new_i = (i + k) % 26
        new_letter = b[new_i]

        if letter.isupper():
            new_letter = new_letter.upper()
        result += new_letter
    else:
        result += letter
print(result)
