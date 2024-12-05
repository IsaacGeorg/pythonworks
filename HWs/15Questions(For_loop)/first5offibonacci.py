
# Print the first 5 elements of fibonacci series using 'for' loop.

n = 5
a, b = 0, 1
print(a)

for i in range(1, n):
    print(b)

    a, b = b, a + b