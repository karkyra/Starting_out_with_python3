# A night club will give you a word. For entrance, you need to provide the right
# number according to the provided word.
# Every given word will have a doubled letter, like "dd" in addiction. To answer
# the right number you need to find the doubled letter's position in the alphabets and
# multiply this number with 4.
# Create a function that takes the argument of word and returns the right number.
import string
def club_entry(word):
    al = dict(zip(string.ascii_lowercase, range(1,27)))

    letter = ""

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            letter = word[i]

    return al[letter] * 4



print(club_entry("hill"))
print(club_entry("apple"))
