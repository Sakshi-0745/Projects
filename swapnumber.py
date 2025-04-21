x = 5
y = 7

print("Before swapping:", x, y)

# Swapping using XOR
x = x ^ y
y = x ^ y
x = x ^ y

print("After swapping:", x, y)
