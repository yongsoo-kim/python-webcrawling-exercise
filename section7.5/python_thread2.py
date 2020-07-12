import threading


class Thread_Run(threading.Thread):
    def run(self):
        print('Thread running - C')


for i in range(1000):
    t = Thread_Run()
    # Start thread
    t.start()
