def a(b):
    try:
        print(c)
    except NameError:
        print("Variable c is not defined")
    except:
        print("Something else went wrong")
d=input('Enter the value:')
a(d)