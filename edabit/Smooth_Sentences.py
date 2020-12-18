# Carlos is a huge fan of something he calls smooth sentences.
# A smooth sentence is one where the last letter of each word is identical to
# the first letter the following word (and not case sensitive, so "A" would be the same as "a").
# The following would be a smooth sentence "Carlos swam masterfully" because "Carlos" ends with
# an "s" and swam begins with an "s" and swam ends with an "m" and masterfully begins with an "m".
# Create a function that determines whether the input sentence is a smooth sentence, returning
# a boolean value True if it is, False if it is not.

def is_smooth(sentence):

    sentence = sentence.lower().split(" ")

    a = all([True if f[-1] == s[0] else False for f ,s in zip(sentence, sentence[1:])  ])
    print(a)

    # for f, s in zip(sentence, sentence[1:]):
    #     print(f[-1],s[0] )



is_smooth("She eats super righteously")
is_smooth("Someone is outside the doorway")
