def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                print('info level log')
            elif level == 'error':
                print('error level log')
        return wrapper
    return decorator


@log(level='error')
def func1():
    print('I am a function1')


@log(level='info')
def func2():
    print('I am a function1')


func1()
func2()
