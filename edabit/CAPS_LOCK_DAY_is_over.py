# October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase,
# so write a function to normalize a sentence.
# Create a function that takes a string. If the string is all uppercase characters, convert
# it to lowercase and add an exclamation mark at the end.

def normalize(txt):
    txt1 = txt.split()
    lst =  [i.lower() for i in txt1 if i.isupper()]
    if lst:
        return "".join(lst[0].capitalize())+ " " + " ".join(lst[1:]) + "!"
    else:
        return txt

print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("Let us stay calm, no need to panic."))
