# Create a function that builds a word from the scrambled letters contained in the first list.
# Use the second list to establish each position of the letters in the first list.
# Return a string from the unscrambled letters (that made-up the word).

def word_builder(ltr, pos):

    # word = ""
    # for i in pos:
    #     word += ltr[i]
    # return word
    return "".join([ltr[i] for i in pos])
print(word_builder(["g", "e", "o"], [1, 0, 2]))
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) )
