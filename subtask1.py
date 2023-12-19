def nqi(n):
    q = 0
    i = 0

    while (i + 1)**2 <= n:
        q = i + 1
        i += 1

    return q

# Example usage:
n = 31
result = nqi(n)
print("The largest square number <", n, "is", result)
