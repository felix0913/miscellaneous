import time
# def producer():
#     ret = []
#     for i in range(100):
#         time.sleep(0.1)
#         ret.append('baozi %s' %i)
#     return ret

# def consumer(res):
#     for index, baozi in enumerate(res):
#         time.sleep(0.5)
#         print('第%s个人，吃了%s' %(index, baozi))

# res = producer()
# consumer(res)


def producer():
   c1 = consumer('felix')
   c2 = consumer('jason')
   c1.__next__()
   c2.__next__()
   for i in range(10):
       c1.send('包子 %s' %i )
       c2.send('包子 %s' %i )

def consumer(name):
    print('我是%s, 我准备开始吃包子了' % name)
    while True:
        baozi = yield
        print('%s 很开心的把%s吃掉了' %(name, baozi))

producer()
