# def product_baozi():
#     for i in range(100):
#         yield '一抽屉包子%s' % i

# pro_g = product_baozi()


def produce_egg():
    # ret = []
    for i in range(100):
        yield 'egg %s ' % i
    return ret

print(produce_egg())