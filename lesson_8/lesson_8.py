#array = [1, 2, 3, 4, 5]
#array_1 = []

#for el in array:
    #array_1.append(el ** 2)
#print(array_1)

#a = [i**2 for i in array]
#print(a)

#a = [ x*2 if x%2==0 else x+1 for x in range(5, 10)]
#print(a)

#a = [x + y for x in range(1, 4) for y in range(5, 10)]
#print(a)

#a = [str(x) + str(y) for x in range(3) for y in range (x+3)]
#print(a)

import random

#r = [ random.randint(-10, 10) for i in range(15)]
#print(r)

#print(len(r))

#print(random.random())

#print(random.randrange(1, 100, 2))


#r = [[1, 2, 1, 1], [1, 2, 3], [1, 1, 14, 5], [1, 1, 1, 1]][::]
#r2 = r[::]
#print(r)
#print(r2)

#r = [[1, 2, 1, 1, 1], [1, 2, 3, 4, 1], [1, 1, 14, 5, 2], [1, 1, 1, 1, 1]]
#print(r[2][2])

#n = 4
#matrix = [ [i for i in range(j,j+n)] for j in range(0, n**2-1, n)]
#print(matrix)




#a = (x*2 if x%2==0 else x+1 for x in range(5, 10))
#print(a)

#for i in a:
    #print(i)


print(sum(x*2 if x%2==0 else x+1 for x in range(5, 10)))

print(any(x*2 if x%2==0 else x+1 for x in range(5, 10)))

print(all(x*2 if x%2==0 else x+1 for x in range(5, 10)))