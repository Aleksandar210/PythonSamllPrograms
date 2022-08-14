def print_hi(name):
    """
    Description of function:
    print_hi functions accepts a str parameter and prints Hi, to that parameter
    to the console

    Arguments:
        name(str) this represents the name that will be used to say Hi to
    """
    print(f'Hi, {name}')


if __name__ == '__main__':
    multidim = [1,2,3,4]
    for _ in range(len(multidim) - 1):
        print(multidim[_])

