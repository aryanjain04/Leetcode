from typing import List

def getNoZeroIntegers(n: int) -> List[int]:
    def has_zero(x):
        return '0' in str(x)

    for a in range(1, n):
        b = n - a
        if not has_zero(a) and not has_zero(b):
            return [a, b]

# Example usage
print(getNoZeroIntegers(101))
print(getNoZeroIntegers(11))
print(getNoZeroIntegers(1000))
