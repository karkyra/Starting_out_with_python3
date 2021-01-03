# One cause for speeding is the desire to shorten the time spent traveling.
#  In long distance trips speeding does save an appreciable amount of time.
#  However, the same cannot be said about short distance trips.
# Create a function that calculates the amount of time saved were you traveling
# with an average speed that is above the speed-limit as compared to traveling with
#  an average speed exactly at the speed-limit.

def time_saved(s_lim, s_avg, d):

    avg = d / s_avg
    lim = d / s_lim

    return abs(round((avg - lim) *60, 1))

print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 10) )
