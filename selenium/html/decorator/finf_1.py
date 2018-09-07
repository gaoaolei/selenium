def foo():
    def bar():
        print('in bar()')

    print('in foo()')
    return bar

inner = foo()
inner()
