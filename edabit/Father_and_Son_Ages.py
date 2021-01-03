# Create a function that takes two arguments of father's current age f_age and son's
# current age s_age. Сalculate how many years ago the father was twice as old as his
 # son OR in how many years he will be twice as old.

def age_difference(f_age, s_age):

    a = f_age - s_age

    return abs(s_age - a)




print(age_difference(36, 7))
print(age_difference(55,30))
print(age_difference(42, 21))
