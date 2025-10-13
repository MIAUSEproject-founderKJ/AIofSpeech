import threading
import time
import random

#shared global variable
recognized_text=None
running=True

def listen_microphone():

  """Simulate microphone input (I/O bound task)"""
  global recognized_text
  while running:
      time.sleep(random.uniform(0.5,1.5)) #simulate variable delay
      recognized_text = random.choice(["turn on the light", "move forward", "stop"])
      print(f"[Mic] Heard:{recognized_text}")

def process_command():
    """Simulate text processing (light CPU)"""
    global recognized_text
    while running:
      if recognized_text = None
    time.sleep(0.5)

def background_monitor():
    """Simulate constant monitoring"""
    while running:
        print("[Monitor] System OK")
        time.sleep(3)

if __name__ == "__main__":
    t1 = threading.Thread(target=listen_microphone)
    t2 = threading.Thread(target=process_command)
    t3 = threading.Thread(target=background_monitor)

    t1.start(); t2.start(); t3.start()

    try:
        time.sleep(10)
    finally:
        running = False
        print("Stopping all threads...")
