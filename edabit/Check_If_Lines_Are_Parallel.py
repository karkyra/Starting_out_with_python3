# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], which corresponds
# to the line ax+by=c.

def lines_are_parallel(l1, l2):
    if(l1[1]!=0 and l2[1]!=0):
        if(l1[0]/l1[1]==l2[0]/l2[1]):
            return True
        else:
            return False
    else:
        if(l1[0]==l2[0] and l1[1]==l2[1]):
            return True
        else:
            return False
print(lines_are_parallel([1, 2, 3], [1, 2, 4]))
