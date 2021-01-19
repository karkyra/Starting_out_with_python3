    # consonants(word) which returns the number of consonants in a word when called.
    # vowels(word) which returns the number of vowels in a word when called.

def consonants(word):

    VOWELS = "aeiou"
    count = 0
    word2 = ''.join([c.lower() for c in word if c.isalpha()])

    for i in word2:
        if i not in VOWELS:
            count +=1
    return count

print(consonants('He|\o mY Fr*end'))

def vowels(word):

    VOWELS = "aeiou"
    count = 0
    word2 = ''.join([c.lower() for c in word if c.isalpha()])

    for i in word2:
        if i in VOWELS:
            count +=1
    return count

print(vowels('Jameel SAEB'))
