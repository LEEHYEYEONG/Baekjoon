word = input()

reverse_word = "".join(reversed(word))
if word == reverse_word:
    print(1)
else:
    print(0)
