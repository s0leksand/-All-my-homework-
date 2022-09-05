import random

my_dict = {random.randint(1,123) for _ in range(21)}
my_dict.sum()
print(my_dict)