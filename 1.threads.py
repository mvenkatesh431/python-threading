import threading

def run():
    print(f"Hello from thread {threading.current_thread()}")

run()
# Hello from thread <_MainThread(MainThread, started 36440)>

# Create a thread using threading 
t = threading.Thread(name="MyThread",target=run)
# start the thread
t.start()
t.join()
# Hello from thread <Thread(MyThread, started 41824)>

