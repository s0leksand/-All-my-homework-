def decorator_function(func):
    import time

    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print(f"[*] it took {stop=start} sec.")

    return wrapper


@decorator_function
def decorator_function():
    print("Hello world")