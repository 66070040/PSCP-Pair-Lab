"""Align"""


def main():
    """Align"""
    space = int(input())
    pos = str(input())
    text = str(input())
    num = space - len(text)
    c_space = int(num/2)
    if pos == "left":
        print(text+" "*num)
    elif pos == "right":
        print(" "*num + text)
    else:
        if num % 2 == 0:
            print(" "*c_space + text +" "*c_space)
        else:
            print(" "*(c_space+1) + text +" "*c_space)


main()
