print("Answer 1:", list(map(lambda x, y=2: x ** y, [3, 6, 9])),
      "\nAnswer 2:", list(map(lambda x, y=2: x ** y, [3, 6, 9], [1, 2, 3])))