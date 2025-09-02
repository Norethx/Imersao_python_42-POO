import sys


def shrink(a_str: str) -> str:
    """cut string and transforma it size in 8"""
    return a_str[0:8]


def enlarge(a_str: str) -> str:
    """fill the string with Z in max size 8"""
    return a_str.ljust(8, "Z")


def main() -> int:
    """Verify size of string receive and cut or fill the string"""
    if len(sys.argv) == 1:
        print(None)
        return 0
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) < 8:
            print(enlarge(sys.argv[i]))
        elif len(sys.argv[i]) > 8:
            print(shrink(sys.argv[i]))
        else:
            print(sys.argv[i])
    return 0


if __name__ == "__main__":
    sys.exit(main())
