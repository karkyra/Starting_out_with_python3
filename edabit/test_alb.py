def Test_ALB(lst):

    txt =""
    for i in lst:
        txt += i.split(":")[0] + " "
    print(txt)

Test_ALB(["a:aa", "b:bb", "c:cc", "d:dd", "f:ff"])
