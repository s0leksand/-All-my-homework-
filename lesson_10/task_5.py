A = {i for i in range(25-10)}
B = {i for i in range(15, 15 + 22 - 10)}
C = {i for i in range(27, 27 + 22 - 10)}

A_B = {i for i in range(33)}
A_C = {i for i in range(64, 64 + 32)}
B_C = {i for i in range(33, 33 + 31)}

print("A і B:", len(A_B - (A | B)))
print("A і C:", len(A_C - (A | C)))
print("B і C:", len((B | C) - B_C))
