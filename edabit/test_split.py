def test_split(lst):

    for i in lst:
        print(i.split(":")[0])


print(test_split(['subnet-033d90734e11d095c: ec2', 'subnet-033d90734e11d44c: ec2', 'subnet-033d90734e11d555c: NLB']))
