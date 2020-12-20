# Create a function based on the input and output. Look at the examples, there is a pattern.
# secret("div*2") ➞ "<div></div><div></div>"
#
# secret("p*1") ➞ "<p></p>"
#
# secret("li*3") ➞ "<li></li><li></li><li></li>"

def secret(text):
    a = text.split("*")
    b = "<" + a[0] + ">" + "</" + a[0] + ">"
    print(b * int(a[1]))

secret("div*2")
secret("p*1")
secret("li*3")
