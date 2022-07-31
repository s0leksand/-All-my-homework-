
# спосіб 1
var1 = 666
var2 = 999
print(var1, var2)

var3 = var1
var1 = var2
var2 = var3
print(var1, var2)

# спосіб 2
var1, var2 = var2, var1
print(var1, var2)

# спосіб 3
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print(var1, var2)
