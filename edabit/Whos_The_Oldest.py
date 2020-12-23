# Given a dictionary containing the names and ages of a group of people,
# return the name of the oldest person.

def oldest(people):

    return  max(zip(people.values(), people.keys()))[1]




print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}) )
