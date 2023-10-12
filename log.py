def timestamp(func):
    def time(*args, **kwargs):
        print(time.ctime())
        result = func(*args, **kwargs)
        return result
    return time
