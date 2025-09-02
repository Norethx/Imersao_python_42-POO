import sys


def main() -> int:
    """print the arguments of the program between NL"""
    for arg in sys.argv:
        print(arg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
