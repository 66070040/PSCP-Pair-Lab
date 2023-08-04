"""Table I"""


def multiplyer(second):
    """Doc"""
    for i in range(1, second + 1):
        print("15 x {0} = {1}".format(i, 15 * i))


multiplyer(int(input()))
