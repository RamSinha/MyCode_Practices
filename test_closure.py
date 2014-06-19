def outer():
    x=1
    def inner():
        print x
    print inner
    return inner


foo=outer()
print foo.func_closure
print dir(foo)
