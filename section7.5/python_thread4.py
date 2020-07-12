# Logging
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s (%(threadName)-8s) %(message)s]',
)


def worker1():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Exiting...')


def worker2():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Exiting...')


# Daemon thread(This threads ends all threads when main thread ended its task.)
t1 = threading.Thread(name="service-1", target=worker1)
t2 = threading.Thread(name="service-2", target=worker2, daemon=True)
t3 = threading.Thread(target=worker1, daemon=True)


if __name__ == "__main__":
    t1.start()
    t2.start()
    t3.start()