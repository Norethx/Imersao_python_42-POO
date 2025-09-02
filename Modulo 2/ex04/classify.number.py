import sys


def is_positive(a: int) -> bool:
    """Receive a int value and return if is positive or negative"""
    return a > 0


def main() -> int:
    """Receive a int value and print if is positive or negative"""
    print(is_positive(int(sys.argv[1])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
