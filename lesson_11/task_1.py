def list_number(a, b):
    for i in a:
        for j in a:
            if a.index(i) != a.index(j) and i + j == b:
                return True
    return False

print("list_number retutn:", list_number([1, 5, 8, 2, 10, 24], 32))
print("list_number retutn:", list_number([1, 7, 6, 4, 10, 22], 4))