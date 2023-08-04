"""Frame"""


def main():
    """Frame"""
    text = str(input())
    size = len(text)
    for i in range(3):
        if i == 1:
            print("*"+text+"*")
        else:
            print("*"*(size+2))


main()
