import datetime
import logging
logging.basicConfig(handlers=[logging.FileHandler('log_out.txt', 'w', 'utf-8')],
                    level=logging.DEBUG)


def decorator(old_func):
    def new_func(*args, **kwargs):
        start = datetime.datetime.now()
        logging.debug('Время вызова: ' + str(start))
        logging.debug('Имя функции: ' + old_func.__name__)
        logging.debug('Аргументы вызова: ' + str(args))
        out_in = old_func(*args, **kwargs)
        out = out_in * 32
        logging.debug('Возвращаемое значение: ' + str(out))
        return out
    return new_func


@decorator
def foo(x, y):
    return x**y

foo(4, 5)
