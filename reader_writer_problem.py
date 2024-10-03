import threading
import time

class ReaderWriter:
    def __init__(self):
        self.readers = 0
        self.lock = threading.Lock()
        self.writer_lock = threading.Lock()

    def reader(self, reader_id):
        while True:
            with self.lock:
                self.readers += 1
                if self.readers == 1:
                    self.writer_lock.acquire()
            print(f"Reader {reader_id} is reading")
            time.sleep(1)  # Simulate reading time
            with self.lock:
                self.readers -= 1
                if self.readers == 0:
                    self.writer_lock.release()
            time.sleep(1)

    def writer(self, writer_id):
        while True:
            self.writer_lock.acquire()
            print(f"Writer {writer_id} is writing")
            time.sleep(2)  # Simulate writing time
            self.writer_lock.release()
            time.sleep(2)

# Example usage:
rw = ReaderWriter()

readers = [threading.Thread(target=rw.reader, args=(i,)) for i in range(3)]
writers = [threading.Thread(target=rw.writer, args=(i,)) for i in range(2)]

for t in readers + writers:
    t.start()
