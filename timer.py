import time

class count_time:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args, **kwargs):
        print('time cost: {0:.3f}s'.format(time.time()-self.start))


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print('[FUNC_NAME]: {0}, [TIME_COST]: {1:.3f}s'.format(f.__name__, time.time()-start))
        return res
    return wrapper