import sys


def downcase_it(v_str: str) -> str:
    """apply lowercase in a str"""
    return v_str.lower()


def main() -> int:
    """receive a arguments and print in lowercase"""
    if len(sys.argv) == 1:
        print(None)
        return 0
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
