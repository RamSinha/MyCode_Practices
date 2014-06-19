## Return the Closures
## Something which will be used later on
## Look Closely how the value was passed to the decorator and was stored in the closure
def outer(some_func):
    def inner(x):
        print "before some_func"
        print 'value is',x
        ret = some_func(x) # 1
        return ret + 1
    return inner
def foo(x):
    return 1
decorated=outer(foo)
print decorated(5)


## Call the actual function and resturn decorated value
def outer1(some_func):
    
    print "before some_func"
    ret = some_func() # 1
    return ret + 1
def foo1():
    return 1
decorated=outer1(foo1)
print decorated

## Also look closely at http://stackoverflow.com/questions/308999/what-does-functools-wraps-do to avoid doc string manipulation
def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func() # 1
        return ret + 1
    return inner
def foo():
    return 1
decorated=outer(foo)
print decorated()




from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print f.__name__  # prints 'f'
print f.__doc__   # prints 'does some math'


