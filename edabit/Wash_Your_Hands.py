# It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
# Create a function that takes the number of times a person washes their hands per
# day N and the number of months they follow this routine nM and calculates the
# duration in minutes and seconds that person spends washing their hands.

def wash_hands(N, nM):

    a = divmod(21 * 30 * N * nM, 60)

    return "{} minutes and {} seconds".format(a[0], a[1])

print(wash_hands(8, 7))
print(wash_hands(7, 9))
print(wash_hands(0, 0))
