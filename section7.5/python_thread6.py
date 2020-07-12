# run task on regular time(Scraping, crawing, checking sth etc...)
import logging
import threading
import time


def thread_run():
    print('=====', time.ctime(), '=====')
    # Code here.
    #########################

    for i in range(1, 10000):
        print('Threading running - ', i)

    #Recursive call 'thread_run' -> Infinite loop
    threading.Timer(2.5, thread_run).start()
    #'forever' package can do similar work.

thread_run()
