def jay_and_bob(txt):

    d = {"half": 0.5, "quarter": 0.25, "eighth": 0.125, "sixteenth": 0.0625}

    for k, v in d.items():
        if k == txt:
            print("{0:.3g} grams".format(v*28))


jay_and_bob("half")
jay_and_bob("eighth")
jay_and_bob("sixteenth")
