def test():
    yield 1
    yield 2
    yield 3

res = test()
print(res.__next__())