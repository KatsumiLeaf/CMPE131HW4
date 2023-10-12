import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        result = func(*args, **kwargs)
        return result
    return wrapper
