# Create a function that transforms a string of upvote counts into a list of numbers.
# Each k represents a thousand.
# Return the upvotes as a list.

def transform_upvotes(txt):

    txt = txt.split()
    return [float(i[:-1]) *1000 if i[-1] =="k" else float(i) for i in txt ]


    # return txt[:-1]

print(transform_upvotes("6.8k 13.5k"))
print(transform_upvotes("5.5k 8.9k 32"))
# print(transform_upvotes("hello"))
