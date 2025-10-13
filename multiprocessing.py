from multiprocessing import Process, Queue
import time
import random

def listen_microphone(q):
  """Simulate microphone input process"""
  while True:
    time.sleep(random.uniform(0.5,1.5))
    text= random.choice(["turn on the light","move forward", "stop"])
    print(f"Mic] Heard: {text}")
    q.put(text)

def process_command(q):
  """Process recognized speech in another process"""
  while True:
    if not q.empty():
      text=q.get()
      print(f"[Processor] Executing command for: {text}")
      time.sleep(0.5)

def background_monitor():
      """Runs independently, isolated process"""
    while True:
        print("[Monitor] System OK")
        time.sleep(3)

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=listen_microphone, args=(q,))
    p2 = Process(target=process_command, args=(q,))
    p3 = Process(target=background_monitor)

    p1.start(); p2.start(); p3.start()

    try:
        time.sleep(10)
    finally:
        print("Terminating processes...")
        p1.terminate(); p2.terminate(); p3.terminate()
  
