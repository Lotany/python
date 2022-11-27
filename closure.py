#first class functions
def square(x):
    return x*x

def cube(x):
    return x *x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

#squares = my_map(cube,[1,2,3,4,5,6,7,8])
#print(squares)

def logger(msg):
    def log_message():
        print("log: " + msg)
    return log_message

#hi = logger("hi")
#hi()

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag,msg))
    return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Test headline')
# print_h1('another headline')

# print_p = html_tag('p')
# print_p('Test paragraph')


#closures

def outer_func(msg1):
    msg = msg1
    def inner_func():
        print(msg)
    return inner_func

# my_func = outer_func('Lotan')
# my_func1 = outer_func('Able')

# my_func()
# my_func1()


import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Runnng "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x -y

# add_logger = logger(add)
# sub_logger = logger(sub)
# add_logger(5,5)
# sub_logger(50,25)

#decorator function

def decorator_function(original_functon):
    def wrapper_function():
        return original_functon()
    return wrapper_function

def display():
    print('Display function run')

decorated_display =decorator_function(display)

decorated_display()