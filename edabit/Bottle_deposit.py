# Compute the refaund amount  for a collection of bottle

LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

less = int(input("How many containers 1 litre or less? "))
more = int(input("How many containers more than 1 litre? "))

refaund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

print("Your total refound will be $%.2f." %refaund)
