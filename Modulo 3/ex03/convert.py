import sys


def main() -> int:
    """receive one parameter and convert your value in float"""
    try:
        print(float(sys.argv[1]))
    except ValueError:
        print("conversion impossible")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
