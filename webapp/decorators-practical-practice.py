# test the performance of my function
import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f'Took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    time.sleep(1)
    my_list = [greet for greet in 'hello']
    return my_list


print(long_time())
