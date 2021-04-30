from datetime import datetime

def log_to_console(func):
    def wrapper(*args, **kwargs):
        date = datetime.date(datetime.now())
        time = datetime.time(datetime.now())
        func_name = func.__name__
        result = func(*args, **kwargs)

        print(f"date: {date}\n"
              f"time: {time}\n"
              f"name: {func_name}\n"
              f"args: {args, kwargs}\n"
              f"result: {result}\n")

        return result
    return wrapper

def log_to_file(log_file):
    def decor(func):
        def wrapper(*args, **kwargs):
            date = datetime.date(datetime.now())
            time = datetime.time(datetime.now())
            func_name = func.__name__
            result = func(*args, **kwargs)

            with open(log_file, 'a', encoding='utf-8') as file:
                file.write(f"date: {date}\n"
                           f"time: {time}\n"
                           f"name: {func_name}\n"
                           f"args: {args, kwargs}\n"
                           f"result: {result}\n")

            return result
        return wrapper
    return decor
