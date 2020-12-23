# Given a musical note, create a function that returns its enharmonic equivalent.
# The examples below should make this clear.

def get_equivalent(note):

    d = {"Db": "C#", "Eb":"D#", "Gb":"F#", "Ab":"G#", "Bb":"A#"}

    for k,v in d.items():
        if note == k:
            return v
        elif note == v:
            return k

print(get_equivalent("D#"))
print(get_equivalent("Gb"))
print(get_equivalent("Bb"))
