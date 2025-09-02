import sys


def square_even_numbers(a_lst: list[int]) -> list[int]:
    """Verify if the element of list is even and apply ** 2 in new list"""
    result: list[int] = []
    for x in a_lst:
        if x % 2 != 1:
             result.append(x ** 2) 
    return result


def main() -> int:
    """Transform the first argument in list of int and print the numbers even ** 2"""
    if len(sys.argv) == 1:
        return 0
    print("Squared evens:", square_even_numbers([int(x) for x in sys.argv[1].split()]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
