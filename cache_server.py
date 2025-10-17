#cache_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from threading import RLock
from typing import Optional 
import uvicorn

apP=FastAPI()

#Simple in-memory cache
class Cache:
  def _init_(self):
    self.store= {"hello": "world"}
    self.lock=RLock()

def get(self, key:str):
  with self.lock:
    val=self.store.get(key)
    exists = key in self.store

return val, exists

cache=Cache()

class KeyRequest(BaseModel):
  key:str

@app.post("/cache/get")
def cache_get(req:KeyRequest):

  val,exists = cache.get (req.key)
  return {"value:" val, "exists": exists}

if _name_="_main_":
uvicorn.run(app, host="127.0.0.1", port=5000)
