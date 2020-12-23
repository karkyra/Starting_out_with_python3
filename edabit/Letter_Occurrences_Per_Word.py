# Create a function that takes in a sentence and a character to find.
#Return a dictionary of each word in the sentence, with the number of the specified character as the value.

def find_occurrences(txt, ch):

    txt2 = set(txt.lower().split())
    all = {}
    for i in txt2:
        all[i] = i.count(ch.lower())

    return all


print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A"))
print(find_occurrences("Create a nice JUICY function", "c"))
