# just uncomment the interested portion of the code and see the results



# example of args                          #output

def args(*a):
    print(a)

# args(1, 2, 3, 4, 5)                    (1, 2, 3, 4, 5)

# s = (1, 2, 3, 4, 5)
# args(*s)                               (1, 2, 3, 4, 5)

def args(a):
    print(a)

# args(1, 2, 3, 4, 5)                     error

# ====================================================================


def kwargs(**a):
    print(a)

# kwargs(a=1, b=2, c=3)                     {'a': 1, 'b': 2, 'c': 3}
# s = {'a': 1, 'b': 2, 'c': 3}
# kwargs(**s)                                 {'a': 1, 'b': 2, 'c': 3}


def kwargs(a):
    print(a)

# kwargs(a=1, b=2, c=3)                          error

