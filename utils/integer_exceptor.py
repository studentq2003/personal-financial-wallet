def integer_exceptor(msg):
    while True:
        try:
            inp = input()
            if inp.isdigit() and int(inp) > 0:
                return int(inp)
            else:
                print(msg)
        except Exception as e:
            print(e)