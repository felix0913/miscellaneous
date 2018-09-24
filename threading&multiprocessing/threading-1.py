import threading
import time

def thread_job():
    print('this is added thread, number is %s' % threading.current_thread())
    print('T1 start\n')
    # for i in range(10):
    #     time.sleep(0.1)
    time.sleep(1)
    print('t1 finish\n')


def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    added_thread.join()
    print('all done\n')

if __name__ == '__main__':
    main()