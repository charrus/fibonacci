import decimal as D
import timeit


def fibonacci1(i: int) -> int:
    if i <= 1:
        return i
    else:
        return fibonacci1(i - 1) + fibonacci1(i - 2)


def fibonacci2(i: int) -> int:
    n1: int = 0
    n2: int = 1
    n3: int = 0

    if i <= 1:
        return i

    for num in range(1, i):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n3


def fibonacci3(i: int) -> int:
    # Credit: https://medium.com/starts-with-a-bang/ask-ethan-what-explains-the-fibonacci-sequence-0dfc9822184f
    # Following the principle that: 1/9899 = 0.0001010203050813213455…
    # with spaces: 1/9899 = 0.00 01 01 02 03 05 08 13 21 34 55…
    # And: 1/99989999 = 0.00000001000100020003000500080013002100340055008901440233037706100987159725844181…
    # with spaces: 1/99989999 = 0.0000 0001 0001 0002 0003 0005 0008 0013 0021 0034 0055 0089 0144 0233 0377 0610 0987 1597 2584 4181…

    if i <= 1:
        return i
    length = len(str(i)) + 1
    length = 2 + (length % 2)

    quotient = 89

    quotient2 = str("{:9^" + str(length * 2) + "}").format(quotient)

    D.getcontext().prec = length * i

    # Strip off the leading 0.
    nums = str(D.Decimal("1") / D.Decimal(quotient2))[2:]

    j: int = int(length * i)
    k: int = int(length * (i + 1))
    num = int(nums[j:k])

    return num


def fibonacci4(i: int) -> int:
    # Credit: https://medium.com/starts-with-a-bang/ask-ethan-what-explains-the-fibonacci-sequence-0dfc9822184f
    # Following the principle that: 1/9899 = 0.0001010203050813213455…
    # with spaces: 1/9899 = 0.00 01 01 02 03 05 08 13 21 34 55…
    # And: 1/99989999 = 0.00000001000100020003000500080013002100340055008901440233037706100987159725844181…
    # with spaces: 1/99989999 = 0.0000 0001 0001 0002 0003 0005 0008 0013 0021 0034 0055 0089 0144 0233 0377 0610 0987 1597 2584 4181…
    #
    # This is a simpler one which is limited to 4 digit integers and uses fewer strings

    if i <= 1:
        return i

    D.getcontext().prec = 1000

    nums = D.Decimal("1") / D.Decimal("99989999")

    # Here we end up with a tuple:
    # (1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 8, 0, 0, 1, 3, 0, 0, 2, 1, 0, 0, 3, 4, 0, 0, 5, 5, 0, 0, 8, 9, ...
    j: int = int(4 * (i - 2) + 1)
    k: int = int(4 * (i - 1) + 1)
    nums_tuple = nums.as_tuple().digits[j:k]
    num = int("".join(str(w) for w in nums_tuple))

    return num


def fibonacci5(i: int) -> int:
    # Credit: https://medium.com/starts-with-a-bang/ask-ethan-what-explains-the-fibonacci-sequence-0dfc9822184f
    # Following the principle that: 1/9899 = 0.0001010203050813213455…
    # with spaces: 1/9899 = 0.00 01 01 02 03 05 08 13 21 34 55…
    # And: 1/99989999 = 0.00000001000100020003000500080013002100340055008901440233037706100987159725844181…
    # with spaces: 1/99989999 = 0.0000 0001 0001 0002 0003 0005 0008 0013 0021 0034 0055 0089 0144 0233 0377 0610 0987 1597 2584 4181…

    if i <= 1:
        return i
    length: int = 2

    quotient: int = 89

    # quotient2 = str("{:9^" + str(length * 2) + "}").format(quotient)
    # Pad either side with 9's:
    quotient_str = str("{:9^4}").format(quotient)

    D.getcontext().prec = 28

    # Strip off the leading 0.
    nums = str(D.Decimal("1") / D.Decimal(quotient_str))[2:]

    j: int = int(length * (i - 0))
    k: int = int(length * (i + 1))
    num = int(nums[j:k])

    return num


def main() -> None:
    num = 10

    print("fibonacci recursive:")
    for i in range(num):
        print(fibonacci1(i))
    print()

    print("fibonacci iterative:")
    for i in range(num):
        print(fibonacci2(i))
    print()

    print("fibonacci quotient:")
    for i in range(num):
        print(fibonacci3(i))
    print()

    print("fibonacci fixed quotient:")
    for i in range(num):
        print(fibonacci4(i))
    print()

    print("fibonacci fixed quotient with strings:")
    for i in range(num):
        print(fibonacci5(i))
    print()

    print("fibonacci recursive timeit:")
    print(timeit.timeit("fibonacci1(10)", setup="from __main__ import fibonacci1"))
    print()

    print("fibonacci iterative timeit:")
    print(timeit.timeit("fibonacci2(10)", setup="from __main__ import fibonacci2"))
    print()

    print("fibonacci quotient timeit:")
    print(timeit.timeit("fibonacci3(10)", setup="from __main__ import fibonacci3"))
    print()

    print("fibonacci fixed quotient timeit:")
    print(timeit.timeit("fibonacci4(10)", setup="from __main__ import fibonacci4"))
    print()

    print("fibonacci fixed quotient with strings timeit:")
    print(timeit.timeit("fibonacci5(10)", setup="from __main__ import fibonacci5"))
    print()


if __name__ == "__main__":
    main()
