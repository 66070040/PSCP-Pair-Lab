"""Hamburger"""


def main():
    """Hamburger"""
    bun_1 = int(input())
    bun_2 = int(input())
    meat = (bun_1 + bun_2) * 2
    print("|"*bun_1 + "*"*meat + "|"*bun_2)


main()
