def Test_ALB(lst):

    # txt = []
    # for i in lst:
    #     txt.append(i.split(":")[0])
    txt = [i.split(":")[0] for i in lst]
    print(" ".join(txt))

Test_ALB(["a:aa", "b:bb", "c:cc", "d:dd", "f:ff"])
