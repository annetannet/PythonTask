import functools
import time


def logging(function):
    @functools.wraps(function)
    def wrapper(*args, kwargs):
        start_time = time.time()
        for i in range(1, 100000000):
            function(*args)
        end_time = time.time()
        work_time = (end_time - start_time)
        print(work_time)
    return wrapper


@logging
def func(x, y, z=0):
    time.sleep(0.5)
    return x * y + z
@logging
def list1():
    s = []
@logging
def list2():
    s = list()

if __name__ == '__main__':
    list1()
    list2()
    # func(1, 2, 3)
    # func({'x': 1, 'y': 2})
    # func(1, [2], {3})