from threading import Thread
import time


def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f'Has been waiting for {count} second(s)...')


t = Thread(target=show_timer, daemon=True)
t.start()

answer = input('Do you want to exit? (Hit Enter):\n')


'''
A daemon thread is a background thread.
A daemon thread is useful for executing tasks that are not critical.
The program can exit and doesn't need to wait for the daemon threads to be completed.
A daemon thread is automatically killed when the program exits.
'''