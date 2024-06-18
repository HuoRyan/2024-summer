def greatest_common_divisor(n, m):
    while m != 0:
        n, m = m, n % m
    return n

def reduce_fraction(n, m):
    gcd = greatest_common_divisor(n, m)
    return n // gcd , m // gcd

def main():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    new_numerator, newdominator = reduce_fraction(numerator, denominator)
    if numerator == new_numerator and denominator == newdominator:
        print(f"The fraction {numerator}/{denominator} cannot be reduced")
    else:
        print(f"The fraction  can be reduced to {new_numerator}/{newdominator}")
main()