# Given a character and a value between 0 and 100, return a string that represents a simple progress bar.
#     The value represents a percentage.
#     The bar should begin and end with "|"
#     Repeat the character to fill the bar, with each character equivalent to 10%
#     Use spaces to pad the bar to a length of 10 characters.
#     A single space comes after the bar, then a message with the % of completion (e.g. "Progress: 60%")
#     If the value is 100, the message should be "Completed!".
# Examples
# progress_bar("#", 0) ➞ "|          | Progress: 0%"
# progress_bar("=", 40) ➞ "|====      | Progress: 40%"
# progress_bar("#", 60) ➞ "|######    | Progress: 60%"
# progress_bar(">", 100) ➞ "|>>>>>>>>>>| Completed!"

def progress_bar(bar, progress):

    if progress == 0:
        return "|          | Progress: {}%".format(progress)
    elif progress == 100:
        return "|{}| Completed!".format(bar *int(progress / 10))
    else:
        return "|{}| Progress: {}%".format(bar *int(progress / 10)+" "* (10 - (int(progress / 10))),int(progress))



print(progress_bar("=", 40))
print(progress_bar("#", 0))
print(progress_bar("#", 60))
print(progress_bar(">", 100))
