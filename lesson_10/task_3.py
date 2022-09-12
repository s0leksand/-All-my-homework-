badge_stamp = {i for i in range(1, 16)}
badge = {i for i in range(35, 23 + 35 - 16)}
stamp = {i for i in range(16, 35)}
children = {i for i in range(1, 52)}

print(len(children - (badge_stamp | stamp | badge)))
