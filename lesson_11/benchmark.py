def benchmark_arg(iters):
    def actual_decorator(func):  # new
        import time

        def wrapper(*args, **kwargs):
            total = 0  # new
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                stop = time.time()
                total = total + (stop-start)

            print(f"[*] average time {total/iters} sec.")
            return return_value

        return wrapper

    return actual_decorator


@benchmark_arg(iters=10)  # new
def fetch_webpage_2(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


url = "https://rozetka.com.ua/"
web_page = fetch_webpage_2(url)
print(web_page)