#move the Cache.Get() function into a separate Python module, but still make it callable from Go main.go file.
# cache_module.py
# Python version of Cache.Get() from Go
import sys
import json
from threading import RLock

class Cache:
  def _init_(self):
    self.store ={}
    self.lock = RLock()

def get (self, key: str):
  """get a value by key safely (like Go's RLock)."""
  with self.lock:
    val= self.store.get(key)
    exists = key in self.store

return val, exists

# Command-line mode
if _name=="_main_":
  if len(sys.argv)<2:
    print(json.dumps({"value":None, "exists": False}))
    sys.exit(0)

key=sys.argv[1]
cache=Cache()
val,exists = cache.get(key)
print(json.dumps({"Value": val, "exists": exists}))
