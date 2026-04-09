def integer_sqrt(n):
    if n < 0:
        raise ValueError("Square root not defined for negative numbers")
    if n == 0 or n == 1:
        return n

    left, right = 0, n
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
print(integer_sqrt(16))  
print(integer_sqrt(10)) 
