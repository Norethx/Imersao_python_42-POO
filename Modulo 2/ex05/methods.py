import sys


def main() -> int:
    """receive a string and return if the method is true or false"""
    print("São maiusculas?", sys.argv[1].isupper())
    print("É númerico?", sys.argv[1].isnumeric())
    print("É ascii?", sys.argv[1].isascii())
    print("É alfanumérico?", sys.argv[1].isalnum())
    return 0


if __name__ == "__main__":
    sys.exit(main())
