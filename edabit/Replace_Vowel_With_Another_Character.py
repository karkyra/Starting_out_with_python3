# Create a function that takes a string and replaces the vowels with another character.
#
#     a = 1
#     e = 2
#     i = 3
#     o = 4
#     u = 5

def replace_vowel(word):
    # vowels = {"a": 1, "e":2, "i": 3, "o":4, "u": 5 }
    # lst = []
    # for k in word:
    #     if k in vowels:
    #         lst.append(vowels[k])
    #     else:
    #         lst.append(k)
    # return "".join(map(str, lst))
    return word.translate(str.maketrans('aeiou', '12345'))
print(replace_vowel("karachi"))
print(replace_vowel("chembur"))
