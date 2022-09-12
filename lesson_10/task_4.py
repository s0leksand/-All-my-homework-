planet_circus = {i for i in range(1, 5)}
gym_circus = {i for i in range(8, 8 + 1)}
planet_gym = {i for i in range(5, 5 + 3)}


planet = {i for i in range(16, 16 + 19)}
sick = {i for i in range(35, 35 + 3)}
gym = {i for i in range(1, 6)}
circus = {i for i in range(6, 6 + 10)}

print(len((planet | circus | sick | gym) - (planet_circus | planet_gym | gym_circus)))
