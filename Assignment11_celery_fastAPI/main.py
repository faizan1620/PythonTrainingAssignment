from modules.task_out import _to_taskout
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from redis.lock import Lock as RedisLock
from modules import task

redis_instance = Redis.from_url(task.redis_url)
lock = RedisLock(redis_instance, name="task_id")

REDIS_TASK_KEY = "current_task"

from modules import task

app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str


@app.get("/start")
def start() -> TaskOut:
    try:
        if not lock.acquire(blocking_timeout=4):
            raise HTTPException(status_code=500, detail="Could not acquire lock")

        task_id = redis_instance.get(REDIS_TASK_KEY)
        print(task_id,task.app.AsyncResult(task_id).ready())
        r = task.dummy_task.delay()
        redis_instance.set(REDIS_TASK_KEY, r.task_id)
        return _to_taskout(r)
    finally:
        lock.release()

@app.get("/status")
def status(task_id: str) -> TaskOut:
    task_id = task_id or redis_instance.get(REDIS_TASK_KEY)
    if task_id is None:
        raise HTTPException(
            status_code=400, detail=f"Could not determine task {task_id}"
        )
    r = task.app.AsyncResult(task_id)
    return _to_taskout(r)

@app.get("/")
def root():
    return {"status": "FastAPI is running"}
